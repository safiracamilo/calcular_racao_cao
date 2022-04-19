import csv
import pytest
from main import calcularRacaoPorteP, calcularRacaoPorteM, calcularRacaoPorteG

@pytest.mark.parametrize('peso,resultado_esperado',[
                            # valores
                            (4, 0.04),
                            (2, 0.02),
                            (7, 0.07),
                            ('a', 'falha ao executar o calculo da racao'),
                            ('@', 'falha ao executar o calculo da racao'),
                         ])
# a função P pega os dados acima
def testar_calcularRacaoPorteP(peso, resultado_esperado):
    # peso = 4
    # resultado_esperado = 0.04

    resultado_atual = calcularRacaoPorteP(peso)
    assert resultado_atual == resultado_esperado

def testar_calcularRacaoPorteM():
    peso = 8
    resultado_esperado = 0.16

    resultado_atual = calcularRacaoPorteM(peso)
    assert resultado_atual == resultado_esperado

def ler_dados_csv():
    dados_csv = []  # criação de uma lista vazia
    nome_arquivo = 'C:/Users/PHILCO/PycharmProjects/calcular_racao_cao/Test/db/massa_porteg.csv'  # local e nome onde está o arquivo de massa
    try:
        with open(nome_arquivo, newline='') as csvfile:  # repetir a leitura até o fim do arquivo
            campos = csv.reader(csvfile, delimiter=',')
            next(campos)
            for linha in campos:
                dados_csv.append(linha)
        return dados_csv
    except FileExistsError:
        print(f'Arquivo não encontrado:{nome_arquivo}')
    except Exception as fail:
        print(f'Falha imprevista:{fail}')

@pytest.mark.parametrize('id,peso,resultado_esperado',ler_dados_csv())
def testar_calcularRacaoPorteG(id,peso,resultado_esperado):
    #peso = 8
    #resultado_esperado = 0.16

    resultado_atual = calcularRacaoPorteG(float(peso))
    assert resultado_atual == float(resultado_esperado)






