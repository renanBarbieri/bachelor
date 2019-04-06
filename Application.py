# -*- coding: utf-8 -*-

from UserInput import UserInput
from BooleanText import BooleanText
# Recuperação da Informação - 2019.1
# Renan Hozumi Barbieri - DRE: 111201610

# Implemente o modelo booleano de recuperação de informação, tendo como entradas:
#   –  Vetor coluna onde cada linha representa o texto de um documento (matriz Nx1)
#   –  Vetor linha de strings (matriz 1xNs), onde o elemento em cada coluna armazena uma stopword
#   –  String contendo os termos da consulta (separados por espaços)
#   –  Vetor linha de caracteres (matriz 1xNc), onde o elemento em cada coluna representa um separador a ser usado na tokenização dos documentos

# Sua implementação deve:
#   –  Tokenizar os documentos utilizando os separadores adequados
#   –  Normalizar termos (ex. caixa-baixa) e eliminar stopwords das consultas e documentos
#   –  Usar uma solução de indexação udlizando uma variação da matriz de incidências (obs.: guarde a frequência de aparecimento dos termos em cada documento)
#   –  Responder consultas puramente conjuntivas e disjuntivas:
#       •  AND entre todos os termos da consulta
#       •  OR entre todos os termos da consulta


class Application(object):

    def __init__(self):

        print("Inicializando a aplicação.")

        inputDocs = UserInput.getDocuments()
        inputSearch = UserInput.getSearch()

        booleanText = BooleanText(inputDocs)
        documentsAND = booleanText.findDocuments(inputSearch, "AND")
        documentsOR = booleanText.findDocuments(inputSearch, "OR")
        print("Documentos encontrados com os termos pesquisados (operação AND): ")
        print(documentsAND)
        print("Documentos encontrados com os termos pesquisados (operação OR): ")
        print(documentsOR)

Application()