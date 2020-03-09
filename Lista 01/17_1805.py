num1, num2 = input().split()
num1, num2 = int(num1), int(num2)

soma = ((num1 + num2) * ((num2 - num1) + 1)) // 2
print(soma)
