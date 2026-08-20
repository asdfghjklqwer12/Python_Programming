# 입출력

a = input()
print(a, end="")
print(type(a))
print(a, type(a), sep=",")

# 정수 변환
a = int(input())
print(a, type(a))

a = int(input())
b = int(input())

print(a, b)

a = input().split()
print(a, type(a))

# map
# map(함수, List 객체)
a = list(map(int, input().split()))
print(a, type(a))
