from cyberjake import check_update, __version__


def test_check_update():
    assert check_update("cyberjake", __version__) is False
    assert check_update("cyberjake", "0.0.0")
    assert check_update("", "0.0.0") is False
