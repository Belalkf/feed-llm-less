import contextlib
import copy
import io
import json
import unittest
from unittest.mock import patch

from scripts.check_hosting import CHECKS, main, validate_rules


def protected_rules():
    return [{'type': 'deletion'}, {'type': 'non_fast_forward'},
            {'type': 'pull_request', 'parameters': {'required_review_thread_resolution': True}},
            {'type': 'required_status_checks', 'parameters': {
                'strict_required_status_checks_policy': True,
                'required_status_checks': [{'context': name, 'integration_id': 15368} for name in sorted(CHECKS)]}},
            {'type': 'code_scanning', 'parameters': {'code_scanning_tools': [
                {'tool': 'CodeQL', 'security_alerts_threshold': 'medium_or_higher', 'alerts_threshold': 'errors'}]}}]


class HostingProtectionTests(unittest.TestCase):
    def test_request_uses_the_new_name_without_changing_settings(self):
        response = io.BytesIO(json.dumps(protected_rules()).encode())
        with patch('scripts.check_hosting.urllib.request.urlopen', return_value=response) as fetch:
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(main(), 0)
        request = fetch.call_args.args[0]
        self.assertEqual(request.get_header('User-agent'), 'Feed-LLM-Less-hosting-check')
        self.assertEqual(request.get_method(), 'GET')
        self.assertEqual(fetch.call_args.kwargs, {'timeout': 20})

    def test_unprotected_branch_is_rejected(self):
        self.assertTrue(validate_rules([]))

    def test_missing_each_required_guard_is_rejected(self):
        rules = protected_rules()
        for index in range(len(rules)):
            with self.subTest(removed=rules[index]['type']):
                self.assertTrue(validate_rules(rules[:index] + rules[index + 1:]))

    def test_missing_platform_spoofed_checks_and_stale_base_are_rejected(self):
        for mutation in ('missing', 'spoofed', 'stale', 'unresolved'):
            rules = copy.deepcopy(protected_rules())
            status = rules[3]['parameters']
            if mutation == 'missing':
                status['required_status_checks'].pop()
            elif mutation == 'spoofed':
                status['required_status_checks'][0]['integration_id'] = None
            elif mutation == 'stale':
                status['strict_required_status_checks_policy'] = False
            else:
                rules[2]['parameters']['required_review_thread_resolution'] = False
            with self.subTest(mutation=mutation):
                self.assertTrue(validate_rules(rules))

    def test_active_guard_accepts_additional_protections(self):
        rules = protected_rules() + [{'type': 'required_signatures'}]
        self.assertEqual(validate_rules(rules), [])

    def test_disabled_or_relaxed_security_scan_is_rejected(self):
        for field, value in [('tool', 'Other tool'), ('security_alerts_threshold', 'high_or_higher'),
                             ('alerts_threshold', 'none')]:
            rules = protected_rules()
            rules[-1]['parameters']['code_scanning_tools'][0][field] = value
            with self.subTest(field=field):
                self.assertTrue(validate_rules(rules))
