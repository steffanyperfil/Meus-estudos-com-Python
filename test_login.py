import pytest

from login import login

def teste_credenciais_validas():
    resposta = login("igor", "senha123")
    assert resposta['success'] == True


def teste_credenciais_nulo():
    resposta = login(" ", " ")
    assert resposta["erro"] == "Nome de usuário ou senha vazio."

def teste_credenciais_invalido():
    resposta = login("ster", "567 ")
    assert resposta["erro"] == "Nome de usuário não existe."


def teste_credenciais_senha_invalida():
    resposta = login("igor", "567 ")
    assert resposta["erro"] == "Senha incorreta."
