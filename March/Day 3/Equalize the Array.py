from collections import Counter

def equalizeArray(arr):
    cnt = Counter(arr)
    
    m_el_num = max(cnt.items(), key = lambda x: x[1])
    
    return len(arr) - m_el_num[1]