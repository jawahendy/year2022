def squares(a, b):
    # Write your code here
    count = math.floor(math.sqrt(b)) - math.floor(math.sqrt(a - 1))
    return count