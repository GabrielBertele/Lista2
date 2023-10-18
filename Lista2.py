import random

class DadoVirtual:
    def __init__(self, faces):
        self.faces = faces

    def rolar(self):
        return random.randint(1, self.faces)

def simular(dado, num_vezes):
    resultados = []
    for _ in range(num_vezes):
        resultado = dado.rolar()
        resultados.append(resultado)
    return resultados

class Calculadora:
    def somar(a, b):
        return a + b

    def subtrair(a, b):
        return a - b

    def multiplicar(a, b):
        return a * b

    def dividir(a, b):
        if b == 0:
            print("Erro: Divisão por zero.")
            return -1
        else:
            return a / b

if __name__ == "__main__":
    dados_faces = [6, 8, 12]
    num_vezes = 3

    for faces in dados_faces:
        dado = DadoVirtual(faces)
        print(f"Dado de {faces} lados:")
        jogadas = simular(dado, num_vezes)
        print("Resultados das tentativas:", jogadas)
        print()

    a = 10
    b = 5

    print("Soma:", Calculadora.somar(a, b))
    print("Subtração:", Calculadora.subtrair(a, b))
    print("Multiplicação:", Calculadora.multiplicar(a, b))
    print("Divisão:", Calculadora.dividir(a, b))
