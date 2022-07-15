N = int(input())
num = list(map(int, input().split()))
num.sort()
len = len(num)
a = len//2
b = num[a]
print(b) 