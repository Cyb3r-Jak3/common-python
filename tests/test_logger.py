import logging
import cyberjake


def test_logger():
    log = cyberjake.make_logger("test")
    log.info("Testing")
    assert isinstance(log, logging.Logger)
