class Vertice:
    def __init__(self, indice, rotulo):
        self.indice = indice
        self.rotulo = rotulo
        self.grau = 0
        self.profundidade_entrada = None
        self.profundidade_saida = None
