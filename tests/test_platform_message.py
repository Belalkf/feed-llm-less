"""Do not promise a working Windows route that has not been checked."""

import contextlib
import io
import unittest
from unittest.mock import patch

from feed_llm_less.cli import main


class PlatformMessageTests(unittest.TestCase):
    def test_windows_refusal_keeps_wsl_unverified(self):
        output = io.StringIO()
        with patch('feed_llm_less.cli.os.name', 'nt'), contextlib.redirect_stderr(output):
            with self.assertRaises(SystemExit) as result:
                main(['--demo'])
        self.assertEqual(result.exception.code, 2)
        self.assertIn('native Windows is unsupported', output.getvalue())
        self.assertIn('WSL is unverified', output.getvalue())


if __name__ == '__main__':
    unittest.main()
