"""
    Manejo de Excepciones
"""

class MiError(Exception):
    """
    """

    def __init__(self, valor):
        self.valor = valor

    def __str__(self):
        return "Lo sentimos pero, existe un error para su valor ingresado: %s %s" %(self.valor,self.valor.__class__)
