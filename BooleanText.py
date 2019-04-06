# -*- coding: utf-8 -*-
import sys
import codecs

class BooleanText(object):

    tokens = []
    docsTk = []
    freqMatrix = {}

    def __init__(self, documents):
        self.docsTk = self._tokenizeDocuments(documents)

    #
    # Encontra os documentos que possuem alguma semelhança com a pesquisa realizada
    #
    def findDocuments(self, search, operation):
        self.tokens = self._tokenize(search)
        self.freqMatrix = self._getTermsFrequency()

        print(self.freqMatrix)

        result = []

        if operation == "AND":
            result = self._intersectAllTerms()
        elif operation == "OR":
            result = self._unionAllTerms()
        else:
            print("Operação não identificada.")

        return list(dict.fromkeys(result))

    #
    # Retorna um array com os tokens identificados no texto
    #
    def _tokenize(self, text):
        text = self._normalize(text)
        text = self._removeSeparators(text)
        words = text.split('-')
        return self._removeStopWords(words)

    #
    # Retorna uma matriz com os documentos com os termos tokenizados
    #
    def _tokenizeDocuments(self, documents):
        matrix = []
        for doc in documents:
            matrix.append(self._tokenize(doc))
        return matrix

    #
    # Normaliza a string passada
    #
    def _normalize(self, text):
        text = text.lower()
        return text

    #
    # Retorna um vetor onde cada elemento é uma stopword
    #
    def _removeSeparators(self, text):
        separators = [' ', ',', '.', '!', '?']

        for separator in separators:
            text = text.replace(separator, '-')

        return text

    #
    # Retorna o array passado sem as stopWords
    #
    def _removeStopWords(self, words):
        stopWords = ['a', 'o', 'e', 'é', '\xc3\xa9', 'de', 'do', 'no', 'são', 's\xc3\xa3o', 'as'] # adicionados dois stopwords extras por conta de codificação

        return [word for word in words if word not in stopWords]

    #
    # Retorna a matriz de incidencia dos termos passados nos documentos passados
    #
    def _getTermsFrequency(self):
        freqs = {}
        for term in self.tokens:
            tFreq = []
            for doc in self.docsTk:
                tFreq.append(doc.count(term))

            freqs.update({ term : tFreq })
        return freqs

    #
    # Itera sob a lista de frequencias e retorna os documentos
    #    que possuem todos os termos da pesquisa
    #
    def _intersectAllTerms(self):
        result = []

        for key, freqArr in self.freqMatrix.items():
            for idx, freq in enumerate(freqArr):
                print(str(idx)+" : "+str(freq))
                if freq == 0:
                    result.append(idx)

        result = list(dict.fromkeys(result)) # demove duplicadas

        return [doc for doc in result if doc not in range(len(self.docsTk))]

    #
    # Itera sob a lista de frequencias e retorna os documentos
    #    que possuem pelo menos um dos termos da pesquisa
    #
    def _unionAllTerms(self):
        result = []

        for key, freqArr in self.freqMatrix.items():
            for idx, freq in enumerate(freqArr):
                if freq > 0:
                    result.append(idx)

        return list(dict.fromkeys(result)) # demove duplicadas