def challenge_01():
    apples = 1729
    oranges = 42
    papaya = apples
    # 1
    apples = apples + oranges
    # 2

def challenge_02():
    apples = 1729
    oranges = 42
    bananas = [apples, oranges]
    # 3

def challenge_03():
    apples = 1729
    oranges = 42
    bananas = [apples, oranges]

    challenge_03_helper(bananas)
    print(bananas)
    print(id(bananas))

def challenge_03_helper(kiwis):
    mangos = 315
    kiwis.append(mangos)
    # 4
    print(kiwis)
    print(id(kiwis))