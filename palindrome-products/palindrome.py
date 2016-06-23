def largest_palindrome(min_factor=1, max_factor=1):
    max_product = 0
    data = {}
    for ii in range (min_factor, max_factor+1):
        for jj in range (ii, max_factor+1):
            product = ii * jj
            if ''.join(reversed(str(product))) == str(product):
                max_product = max(max_product, product);
                data[product] = { ii, jj }
    return max_product, data[max_product]
 
 
def smallest_palindrome(min_factor=1, max_factor=1):
    min_product = 10 ** 10
    data = {}
    for ii in range (min_factor, max_factor+1):
        for jj in range (ii, max_factor+1):
            product = ii * jj
            if ''.join(reversed(str(product))) == str(product):
                min_product = min(min_product, product);
                data[product] = { ii, jj }
    return min_product, data[min_product]
