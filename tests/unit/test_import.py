"""Import tests for cheetah_py."""


def test_import_api_version() -> None:
    """Verify a symbol can be imported from cheetah_py."""
    from cheetah_py import CH_API_VERSION  # noqa: PLC0415

    assert CH_API_VERSION > 0
