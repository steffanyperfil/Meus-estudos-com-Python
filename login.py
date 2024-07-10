banco = {
        "igor":"senha123",
        "steffany": "321"
    }


def login(usuario, senha):

    if usuario.strip() == "" or senha.strip() == "":
        return {"erro": "Nome de usuário ou senha vazio."}
    if not usuario in banco:
        return {"erro": "Nome de usuário não existe."}
    if banco[usuario] != senha:
        return {"erro": "Senha incorreta."}

    return {"success": True}