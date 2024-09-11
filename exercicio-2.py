def gera_fibbonaci(n):

    sequencia_fibbonaci = [0, 1]

    while sequencia_fibbonaci[-1] < n:
        proximo_fibbonaci = sequencia_fibbonaci[-1] + sequencia_fibbonaci[-2]
        sequencia_fibbonaci.append(proximo_fibbonaci)

    return sequencia_fibbonaci

def pertence_fibbonaci(numero):

    sequencia_fibbonaci = gera_fibbonaci(numero)

    if numero in sequencia_fibbonaci:
        return f"O número {numero} pertence à sequência de Fibonacci."
    else:
        return f"O número {numero} NÃO pertence à sequência de Fibonacci."

def main():
    numero = int(input("Informe um número: "))
    print(pertence_fibbonaci(numero))

main()