"""Version tests for cheetah_py."""

from importlib.metadata import version

from cheetah_py import CH_API_VERSION


def test_project_version_matches_api_version() -> None:
    """
    Verify a the prject version matches the API version.

    Cheetah API version comes in two bits, major and minor.
    This python project respects those two and extends them with another element to
    allow for bugfixes outside the vendored code.

    Meaning the major and minor are always expected to match.
    The shift version calculation is described in `cheetah_py.py`.
    """
    project_version_string = version("cheetah_py")
    (project_major, project_minor, _) = project_version_string.split(".", maxsplit=2)

    assert (int(project_major) << 8) | int(project_minor) == CH_API_VERSION
