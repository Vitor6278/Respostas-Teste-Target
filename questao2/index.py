def pertence_fibonacci(num):
    a, b = 0, 1
    while b <= num:
        if b == num:
            return True
        a, b = b, a+b
    return False

numero = int(input("Digite um número: "))
if pertence_fibonacci(numero):
    print(numero, "pertence à sequência de Fibonacci.")
else:
    print(numero, "não pertence à sequência de Fibonacci.")