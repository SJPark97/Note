T = int(input())
for Tc in range(1,T + 1):
    a = input()
    if a == a[::-1]:
        print(f'#{Tc} 1')
    else:
        print(f'#{Tc} 0')