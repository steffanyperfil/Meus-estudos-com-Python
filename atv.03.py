def print_diamond(n):
    # Parte superior do diamante
    for i in range(1, n + 1):
        print('* ' * i)
    # Parte inferior do diamante
    for i in range(n - 1, 0, -1):
        print('* ' * i)

# Definir o número de linhas para a parte superior do diamante
n = 5
print_diamond(n)