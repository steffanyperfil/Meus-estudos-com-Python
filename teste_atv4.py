import pytest
from atv04 import aposentar

def test_aposentaria_positivo():
    resultado = aposentar(1963)
    assert resultado == False

def test_aposentaria_positivo():
    resultado = aposentar(1962)
    assert resultado == False