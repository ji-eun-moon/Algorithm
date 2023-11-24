numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
left = [1, 4, 7]
right = [3, 6, 9]
def solution(numbers, hand):
    N = len(numbers)
    current_left = [3, 0]
    current_right = [3, 2]
    answer = ''
    for i in range(N):
        if numbers[i] == 0:
            position = [3, 1]
        else:
            position = [(numbers[i]-1) // 3, (numbers[i]-1) % 3]
        if numbers[i] in left:
            answer += 'L'
            current_left = position
        elif numbers[i] in right:
            answer += 'R'
            current_right = position
        else:
            left_distance = abs(position[0] - current_left[0]) + abs(position[1] - current_left[1])
            right_distance = abs(position[0] - current_right[0]) + abs(position[1] - current_right[1])
            if left_distance > right_distance:
                answer += 'R'
                current_right = position
            elif left_distance < right_distance:
                answer += 'L'
                current_left = position
            else:
                if hand == 'right':
                    answer += 'R'
                    current_right = position
                else:
                    answer += 'L'
                    current_left = position
    return answer

print(solution(numbers, hand))
