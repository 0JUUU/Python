# 변수 선언
numbers = [1,2,3,4,5,6]
r_num = reversed(numbers)


# reversed_numbers 를 출력
print("reversed_nubmers :", r_num)
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))

# reversed() 함수는 리스트를 바로 리턴 X --> 이터레이터를 리턴 (메모리의 효율성을 위해)