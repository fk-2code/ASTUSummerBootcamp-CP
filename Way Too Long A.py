n = int(input())
words = []

for i in range(n):
    word = input()
    words.append(word)

for i in range(len(words)):
    y= len(words[i])
    if y > 10:
        print(f"{words[i][0]}{y-2}{words[i][y-1]}")
    else:
        print(words[i])
