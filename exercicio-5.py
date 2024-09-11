def inverter_string(string):
    # cria uma string vazia para armazenar o resultado
    string_invertida = ""
    
    # atravessa a string original de trás pra frente e armazena na string invertida
    for i in range(len(string) - 1, -1, -1):
        string_invertida += string[i]
    
    return string_invertida

def main():
    string_original = input("Escreva a string a ser invertida: ")
    string_original = inverter_string(string_original)
    print(f"String original: {string_original}")

main()