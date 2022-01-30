if __name__ == '__main__':
    pelajar = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        pelajar.append([name, score])
    pelajar = sorted(pelajar, key = lambda x: x[1])
    second_lowest_score = sorted(list(set([x[1] for x in pelajar])))[1]
    desired = []
    for stu in pelajar:
        if stu[1] == second_lowest_score:
            desired.append(stu[0])
    print("\n".join(sorted(desired)))