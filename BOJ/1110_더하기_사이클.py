N = input()

if len(N) == 1:
    A = N + N
else:
    B = int(N[0]) + int(N[1])
    if B <= 9:
        A = N[1] + str(B)
    else:
        A = N[1] + str(B)[1]
cnt = 1

while int(A) != int(N):
    C = A
    if len(C) == 1:
        A = C + C

    else:
        B = int(C[0]) + int(C[1])
        # print("B : " + str(B))
        if B <= 9:
            A = C[1] + str(B)
        else:
            A = C[1] + str(B)[1]

    cnt += 1

print(cnt)
