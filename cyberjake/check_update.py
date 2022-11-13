"""Script to check for available updates."""
import json

from packaging.version import Version

try:
    import requests

    REQUESTS_PRESENT = True
except ModuleNotFoundError:
    REQUESTS_PRESENT = False


def check_update(project_name: str, current_version: str) -> bool:
    """Check version against pypi.org information

    **Requires Requests**

    :param project_name: Name of project to check
    :param current_version: Current version of project. Usually from __version__
    :return: Latest version is newer. Returns false if project can't be found
    :rtype: bool
    """
    if not REQUESTS_PRESENT:
        raise ModuleNotFoundError("Requests module needed")

    try:
        latest = Version(
            requests.get(f"https://pypi.org/pypi/{project_name}/json", timeout=10).json()["info"][
                "version"
            ],
        )
    except json.decoder.JSONDecodeError:
        return False
    current_version = Version(current_version)
    return latest > current_version
