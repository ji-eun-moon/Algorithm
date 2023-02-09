T = int(input())
for test_case in range(1, T + 1):
    tc, N = input().split()
    num = ['ZRO', 'ONE', 'TWO', 'THR', "FOR", 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    lst = list(input().split())
    num_dic = {}

    # 숫자 개수 세는 딕셔너리 만들기
    for i in range(10):
        num_dic[num[i]] = lst.count(num[i])

    print(tc)
    # 숫자 갯수 만큼 num 리스트 순서대로 출력
    for i in range(10):
        for j in range(num_dic[num[i]]):
            print(num[i], end=' ')