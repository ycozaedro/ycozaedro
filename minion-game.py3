def minion_game(string):
    L = len(string)
    Stuart = 0
    Kevin = 0
    vowels = "AEIOU"
    for i in range(0,L):
        if string[i] in vowels:
            Kevin += L-i                   #Each letter after string[i]
        else:                              #gives another word
            Stuart += L-i
    if Stuart>Kevin:
        print("Stuart " + str(Stuart))
    elif Stuart<Kevin:
        print("Kevin " + str(Kevin))
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
