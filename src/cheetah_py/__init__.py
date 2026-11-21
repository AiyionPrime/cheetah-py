"""An architecture dependent import of shared objects."""

import platform

_arch = platform.machine().lower()
if _arch in ("aarch64", "arm64"):
    from .vendor.v4_00.arm64.cheetah_py import *
elif _arch == "i686":
    from .vendor.v4_00.i686.cheetah_py import *
else:
    from .vendor.v4_00.x86_64.cheetah_py import *
