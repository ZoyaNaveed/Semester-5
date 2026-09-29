
def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        result = n
    else:
        result = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    memo[n] = result
    return result

n = int(input("Enter the value of n: "))
if n < 0:
    print("Please enter a non-negative integer.")
else:
    fib_series = [fibonacci(i) for i in range(n + 1)]
    print(f"Fibonacci series up to {n}: {fib_series}")

