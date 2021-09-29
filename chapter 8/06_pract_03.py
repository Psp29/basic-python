def addition_recur(n):
    if(n == 0):   # Base condition (important: if not given the function will infinately call itself)
        return 0
    return n + addition_recur(n-1)  # Recursive function


a = addition_recur(5)
print(a)
