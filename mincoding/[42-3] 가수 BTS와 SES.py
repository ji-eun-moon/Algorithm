words = ['BTS', 'SBS', 'BS', 'CBS', 'SES']

word = input()

Min = 21e8
def dfs(level, word):
    global Min
    if len(word) == 0:
        Min = min(level, Min)
        return
    for i in range(5):
        if words[i] in word:
            dfs(level+1, word.replace(words[i], ''))

dfs(0, word)
print(Min)