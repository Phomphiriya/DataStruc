def torWord(inp):
    ls = []
    temp = ""
    for i in inp:
        word = i.split()
        if word[0] == "P":
            if ls == []:
                temp = word[1]
                ls.append(temp)
                print("'{}' -> {}".format(word[1],ls))
            else:
                old = temp[len(temp)-2:]
                new = word[1][0:2]
                old = old.lower()
                new = new.lower()
                if old == new:
                    ls.append(word[1])
                    temp = word[1]
                    print("'{}' -> {}".format(word[1],ls))
                else:
                    print("'{}' -> game over".format(word[1]))
                    return
        elif word[0] == "R":
            ls = []
            print("game restarted")
        elif word[0] == "X":
            return
        else:
            print("'{}' is Invalid Input !!!".format(i))
            return

print("*** TorKham HanSaa ***")
inp = list(map(str,input("Enter Input : ").split(',')))
torWord(inp)

# *** TorKham HanSaa ***
# Enter Input : P Apple,P LEMON,R,P onion,X
# 'Apple' -> ['Apple']
# 'LEMON' -> ['Apple', 'LEMON']
# game restarted
# 'onion' -> ['onion']

# *** TorKham HanSaa ***
# Enter Input : P Apple,P LEMON,R,P onion,X
# 'Apple' -> ['Apple']
# 'LEMON' -> ['Apple', 'LEMON']
# game restarted
# 'onion' -> ['onion']

# *** TorKham HanSaa ***
# Enter Input : P apple,p lemon,P onion,X
# 'apple' -> ['apple']
# 'p lemon' is Invalid Input !!!

# *** TorKham HanSaa ***
# Enter Input : P apPLE,P leMON,R,P Durian,P ant,P pineapple,X
# 'apPLE' -> ['apPLE']
# 'leMON' -> ['apPLE', 'leMON']
# game restarted
# 'Durian' -> ['Durian']
# 'ant' -> ['Durian', 'ant']
# 'pineapple' -> game over