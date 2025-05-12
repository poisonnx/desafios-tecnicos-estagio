def pertence_fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return n == b or n == 0

num = 21  # Pode alterar aqui
if pertence_fibonacci(num):
    print(f"{num} pertence à sequência de Fibonacci.")
else:
    print(f"{num} NÃO pertence à sequência de Fibonacci.")
