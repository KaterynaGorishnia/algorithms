def fibonacci(n: int) -> int:
    num1 = 0
    num2 = 1    
    if n == 0:
        return 0 
    
    for i in range(2, n):
        num1, num2 = num2, num1 + num2
    
    return num1 + num2

n = int(input("Enter the element number in the Fibonacci sequence: "))
result = fibonacci(n)
print(f"The Fibonacci number under the number {n} is equal to: {result}")
