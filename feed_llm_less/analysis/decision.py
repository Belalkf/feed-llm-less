"""Language-independent review routes; path hints never prove architecture."""

from pathlib import PurePosixPath

CONNECTED = {".json", ".jsonl", ".lock", ".pbxproj", ".svg", ".xml", ".toml", ".yaml", ".yml"}
GENERATED = {"package-lock.json", "yarn.lock", "poetry.lock", "Cargo.lock"}


def classify(path):
    item = PurePosixPath(path)
    if any(part.lower() in {"vendor", "vendored", "generated", "dist", "build", "node_modules"}
           for part in item.parts) or item.name in GENERATED:
        return "generated-or-vendor-path"
    if item.suffix.lower() in CONNECTED:
        return "connected-format"
    return "needs-content-review"


def decide(row):
    category = classify(row["path"])
    result = {"action": "inspect", "confidence": "measurements and path hints only", "category": category,
              "summary": "Read what the code does and how it connects before choosing split, keep, or combine.",
              "steps": ["Read callers, shared state, setup, public routes and affected tests.",
                        "Read only the needed parts first if splitting would make the code harder to follow."],
              "related": []}
    if category != "needs-content-review":
        result.update(action="check-owner", summary="Check the tool or file format before making changes.",
                      steps=["This path is a hint, not proof that a tool made the file or that it must stay together.",
                             "Keep the original format. Change its source, or combine files only in supported ways."])
    return result
