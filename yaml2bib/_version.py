from pathlib import Path

import versioningit

REPO_ROOT = Path(__file__).parent.parent
try:
    __version__ = versioningit.get_version(project_dir=REPO_ROOT)
except versioningit.errors.NotVersioningitError:
    __version__ = "unknown"
