"""Integrity Tests of vendored files."""

from hashlib import file_digest
from importlib import resources

import pytest


@pytest.mark.parametrize(
    ("module", "file_name", "expected_sha256"),
    [
        (
            "cheetah_py.vendor.v4_00.arm64.cheetah_py",
            "cheetah_py.py",
            "e5ab4209f20562fcac01af886e95a41f34f38da04c7ec49c4bc80b34d989765e",
        ),
        (
            "cheetah_py.vendor.v4_00.arm64.cheetah_py",
            "cheetah.so",
            "00294d3c270647cf90cca99c1496ae0ae9ee0a3742b8c93017af37a9e9718786",
        ),
        (
            "cheetah_py.vendor.v4_00.i686.cheetah_py",
            "cheetah_py.py",
            "e5ab4209f20562fcac01af886e95a41f34f38da04c7ec49c4bc80b34d989765e",
        ),
        (
            "cheetah_py.vendor.v4_00.i686.cheetah_py",
            "cheetah.so",
            "aefe371619fe7fd7888a9390860febeee6225e894967291c6b0b2a730f471860",
        ),
        (
            "cheetah_py.vendor.v4_00.x86_64.cheetah_py",
            "cheetah_py.py",
            "e5ab4209f20562fcac01af886e95a41f34f38da04c7ec49c4bc80b34d989765e",
        ),
        (
            "cheetah_py.vendor.v4_00.x86_64.cheetah_py",
            "cheetah.so",
            "0239483a6972dd42d9d0d2fc5a3b5935e1e7b92dac9236d7e1f62f84b64e4bee",
        ),
        (
            "cheetah_py.vendor.v4_00",
            "LICENSE.txt",
            "90ee92c27ef8ac9442a7939643d3f0462164f4fef2b72e1ef65be3d418bc5e99",
        ),
    ],
)
def test_vendored_files_from_archives(
    module: str,
    file_name: str,
    expected_sha256: str,
) -> None:
    """
    Verify the integrity of the unmodified vendored files.

    Originally provided at https://www.totalphase.com/products/cheetah-api/
    """
    path = resources.files(module) / file_name
    with path.open(mode="rb") as handle:
        digest = file_digest(handle, "sha256")
        assert digest.hexdigest() == expected_sha256
