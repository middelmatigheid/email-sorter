import pytest
from src.internal.logger.logger import Logger

def test_logger_levels():
    info_logger = Logger("info",None)
    error_logger = Logger("error",None)
    none_logger = Logger(None,None)

    assert info_logger.level == 0
    assert error_logger.level == 1
    assert none_logger.level == 2

def test_logger_another_level():
    with pytest.raises(ValueError):
        Logger("another",None)

def test_logger_wrong_extension():
    with pytest.raises(ValueError):
        Logger("info", "logs.csv")

def test_info_message(capsys):
    logger = Logger("info", None)
    logger.info("message")
    printed_text = capsys.readouterr()

    assert "INFO" in printed_text.out
    assert "message" in printed_text.out

def test_not_info_message_if_error(capsys):
    logger = Logger("error", None)
    logger.info("message")

    printed_text = capsys.readouterr()

    assert printed_text.out == ""

def test_error_message(capsys):
    logger = Logger("error", None)
    logger.error("message")
    printed_text = capsys.readouterr()

    assert "ERROR" in printed_text.out
    assert "message" in printed_text.out

def test_stats_message(capsys):
    logger = Logger(None, None)
    logger.stats("statistic")
    printed_text = capsys.readouterr()

    assert "STATS" in printed_text.out
    assert "statistic" in printed_text.out

def test_writes_to_file(tmp_path):
    logs_file = tmp_path / "logs.txt"

    logger = Logger("info", str(logs_file))
    logger.info("message")

    result = logs_file.read_text(encoding="utf-8")

    assert "INFO" in result
    assert "message" in result
