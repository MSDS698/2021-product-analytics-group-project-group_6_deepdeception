from application import *


def test():
    assert test_predict("I love you") == "0% Deceptive"
    assert test_predict("Pineapples go well on Pizza") == "100% Deceptive"
