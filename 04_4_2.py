# 리스트 내포 사용한 코드
output = [i for i in range(1,101) if "{:b}".format(i).count("0") == 1]

for i in output :
    print("{} : {}".format(i, "{:b}".format(i)))

print("합계:",sum(output))