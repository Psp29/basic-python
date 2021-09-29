def factorial_recur(n):
    if(n == 1 or n == 0):   # Base condition (important: if not given the function will infinately call itself)
        return 1
    return n * factorial_recur(n-1)  # Recursive function


f = factorial_recur(0)
print(f)
