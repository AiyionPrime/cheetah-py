# cheetah-py

This is a minimalistic *SEPARATE WORK* of the Total Phase Cheetah API.

The unmodified files

- `src/cheetah_py/vendor/v4_00/arm64/cheetah_py.py`
- `src/cheetah_py/vendor/v4_00/i686/cheetah_py.py`
- `src/cheetah_py/vendor/v4_00/x86_64/cheetah_py.py`

contain their license texts at the files beginning.

- `src/cheetah_py/vendor/v4_00/arm64/cheetah.so`
- `src/cheetah_py/vendor/v4_00/i686/cheetah.so`
- `src/cheetah_py/vendor/v4_00/x86_64/cheetah.so`

Publishing them adheres to the EULA shipped under
`src/cheetah_py/vendor/v4_00/LICENSE.txt`.

## Pending Scope

### Phase 1
- transparent architecture dependent import
- document checksums of unaltered files
- document update process (how to integrate future api versions)
- test for expected constants, functions and classes
- test for importability
- test for checksum validity of vendored artifacts
- explain chosen licenses and their scope in readme
- invite totalphase's devs to the repository

### Phase 2
- ruff
- mypy
- provide typehints

### Phase 3
- publish to pypi upon tags
- document where it got published
- document how to install it

### Phase 4
- test for functionality on verified vendor hardware
- report results publicly
- document test setup
