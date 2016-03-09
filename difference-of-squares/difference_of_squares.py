def difference(n):
    return square_of_sum(n) - sum_of_squares(n)

def sum_of_squares(n):
    return sum(k**2 for k in range(1, n+1))
    
def square_of_sum(n):
    return sum(k for k in range(1, n+1)) ** 2
