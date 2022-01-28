if __name__ == '__main__':
    N = int(input())
    Out = [];
    for i in range(0,N):
        hen = input().split();
        if hen[0] == "print":
            print(Out)
        elif hen[0] == "insert":
            Out.insert(int(hen[1]),int(hen[2]))
        elif hen[0] == "remove":
            Out.remove(int(hen[1]))
        elif hen[0] == "pop":
            Out.pop();
        elif hen[0] == "append":
            Out.append(int(hen[1]))
        elif hen[0] == "sort":
            Out.sort();
        else:
            Out.reverse();