from itertools import combinations

stuart = 0
kevin = 0

def minion_game(test_str):
    global stuart
    global kevin

    res = [test_str[x:y] for x, y in combinations(range(len(test_str) + 1), r=2)]
    for i in res:
        if i[0] in 'aeiouAEIOU':
            kevin = kevin + 1
        elif i[0] in 'qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM':
            stuart = stuart + 1

    if (kevin > stuart):
        print("Kevin " + str(kevin))
    elif (stuart > kevin):
        print("Stuart " + str(stuart))
    elif(stuart==kevin):
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)