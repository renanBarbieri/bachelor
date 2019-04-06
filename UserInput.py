# -*- coding: utf-8 -*-
from BooleanText import BooleanText

class UserInput(object):

    #
    # Retorna um vetor onde cada elemento representa um documento (e seu texto)
    #
    @classmethod
    def getDocuments(cls):
        # raw_input("Insira os documentos a serem pesquisados:")

        docs = [
            'O peã e o caval são pec de xadrez. O caval é o melhor do jog.',
            'A jog envolv a torr, o peã e o rei.',
            'O peã lac o boi',
            'Caval de rodei!',
            'Polic o jog no xadrez.'
        ]

        return docs

    #
    # Retorna um vetor onde cada elemento é um termo da pesquisa
    #
    @classmethod
    def getSearch(cls):
        query = "xadrez peã caval torr"
        # query = "Quais são as insplicações do trabalho no semestre"

        # query = raw_input("O que deseja buscar nos documentos? ")
        return query

