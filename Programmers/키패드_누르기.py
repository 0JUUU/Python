def solution(numbers, hand):
    answer = ''
    left_hand = 10
    right_hand = 12

    for number in numbers:
        if number == 1 or number == 4 or number == 7:
            answer += "L"
            left_hand = number
        elif number == 3 or number == 6 or number == 9:
            answer += "R"
            right_hand = number
        else:
            if number == 0:
                number = 11
            right_cmp = abs(right_hand-number) % 3 + abs(right_hand-number) // 3
            left_cmp = abs(left_hand-number) % 3 + abs(left_hand-number) // 3
            # print("right_cmp : {} , left_cmp : {}".format(right_cmp, left_cmp))
            if left_cmp < right_cmp:
                left_hand = number
            elif right_cmp < left_cmp:
                right_hand = number
            else:
                if hand == "right":
                    right_hand = number
                else:
                    left_hand = number
            
            if right_hand == number:
                 answer += "R"
            else:
                answer += "L"

    return answer

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]	
hand = "right"
print(solution(numbers, hand))

numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]	
hand = "left"
print(solution(numbers, hand))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
hand = "right"
print(solution(numbers, hand))