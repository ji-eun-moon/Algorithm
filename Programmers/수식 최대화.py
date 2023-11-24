expression = "100-200*300-500+20"
operator_lst = ['+', '-', '*']
priority_lst = []
priority = [0]*3
used = [0]*3
# 우선 순위 정하기
def get_priority(level):
    if level == 3:
        # 우선 순위
        priority_lst.append(priority[:])
        return
    for i in range(3):
        if used[i] == 0:
            used[i] = 1
            priority[level] = operator_lst[i]
            get_priority(level+1)
            used[i] = 0

get_priority(0)

def solution(expression):
    answer = 0
    for i in range(6):
        temp = priority_lst[i]
        nums1 = expression.split(temp[0])
        print(nums1)
        nums2 = []
        for num in nums1:
            nums2 += num.split(temp[1])
        print(nums2)
        nums3 = []
        for num in nums2:
            nums3 += num.split(temp[2])
        print(nums3)
    return answer


print(solution(expression))