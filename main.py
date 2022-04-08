import numbers

def calcularRacaoPorteP(peso):

    if (peso <= 0) or (peso>= 100):
        print('Peso não permitodo: menor ou igual a 0 ou peso acima de 100: __')

    if (peso <= 0) or (peso >= 100):
        print('Peso não permitodo: menor ou igual a 0 ou peso acima de 100')
        return 0
    else:
        resultado = peso * 0.01
        return resultado

def calcularRacaoPorteM(peso):

    if (peso <= 0) or (peso>= 100):
        print('Peso não permitodo: menor ou igual a 0 ou peso acima de 100: __')

    if (peso <= 0) or (peso >= 100):
        print('Peso não permitodo: menor ou igual a 0 ou peso acima de 100')
        return 0
    else:
        resultado = peso * 0.02
        return resultado

def calcularRacaoPorteG(peso):

    if (peso <= 0) or (peso>= 100):
        print('Peso não permitodo: menor ou igual a 0 ou peso acima de 100: __')

    if (peso <= 0) or (peso >= 100):
        print('Peso não permitodo: menor ou igual a 0 ou peso acima de 100')
        return 0
    else:
        resultado = peso * 0.03
        return resultado

if __name__ == '__main__':

    pesoDigitado = input('Digite o peso do cão, devendo ser maior que "0" e abaixo de "100": ')
    pesoConvertido = float(pesoDigitado)
    respostapergunta = " "

    while not isinstance(pesoConvertido, numbers.Real):
       pesoDigitado = input('Digite o peso do cão, devendo ser maior que "0" e abaixo de "100": ')

    print(' Escolha Uma Opção abaixo: ')
    print(' "P" - Pequeno')
    print(' "M" - Médio')
    print(' "G" - Grande')
    print(' Ou "Z" para sair')

    while respostapergunta.upper() != 'Z':

        respostapergunta = input('Escolha sua opção entre P, M, G ou Z para sair: ')

        if respostapergunta.upper() == 'P':
            print('A quantidade de ração para o porte P é: ', calcularRacaoPorteP(float(pesoDigitado)))
        elif respostapergunta.upper() == 'M':
            print('A quantidade de ração para o porte M é: ', calcularRacaoPorteM(float(pesoDigitado)))
        elif respostapergunta.upper() == 'G':
            print('A quantidade de ração para o porte G é: ', calcularRacaoPorteG(float(pesoDigitado)))
        elif respostapergunta.upper() == 'Z':
            break
        else:
            print('Opção inválida')

        exit()






