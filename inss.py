def aposentar(nome, data):
    if data >= 1963:
        aposenta = 2024 - data
        resultado = 65 - aposenta
        print(f'{nome} você ainda não pode se aposentar falta {resultado} anos.')
    elif data <= 1962:
        print(f'{nome}, parabens você já pode se aposentar!!!')
    else:
        print('Coloque um numero valido!')


nome = str(input('Digite seu nome completo por gentileza: '))
data = int(input('Digite seu ano de nascimento para a verificação: '))
aposentar(nome, data)




