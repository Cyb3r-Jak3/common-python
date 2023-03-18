from cyberjake import str2bool


def test_str2bool_true():
    assert str2bool("true")
    assert str2bool("t")
    assert str2bool("yes")
    assert str2bool("y")
    assert str2bool("1")


def test_str2bool_false():
    assert str2bool("n") is False
