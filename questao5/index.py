def inverter_string(s):
    resultado = ""
    for char in reversed(s):
        resultado += char
    return resultado

entrada = input("Digite uma string: ")
print(f"String invertida: {inverter_string(entrada)}")