def libraryFine(d1, m1, y1, d2, m2, y2):
    # Write your code here
    fine = 0
    
    if y1 > y2:
        fine = 10000
    elif m1 > m2 and y1 == y2:
        fine = 500 * (m1 - m2)
    elif d1 > d2 and m1 == m2 and y1 == y2:
        fine = 15 * (d1 - d2)
        
    return fine