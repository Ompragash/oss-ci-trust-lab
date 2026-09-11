import time


def test_allow_base_change_during_execution():
    """Give the POC coordinator time to move upstream main after preparation."""
    time.sleep(45)
    assert True
