from m1_base import Config

def test_config_debug_default():
    assert Config().debug == False
