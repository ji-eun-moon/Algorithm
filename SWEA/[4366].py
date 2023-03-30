T = int(input())

for test_case in range(1, T+1):
    binary = list(map(int, input()))
    trinary = list(map(int, input()))

    binary.sort(reverse=True)
    trinary.sort(reverse=True)

    