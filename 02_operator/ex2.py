# 비트 연산자
a = 5  # 00000101
b = 3  # 00000011
print(a & b)  # 00000001
print(a | b)  # 00000111
print(a ^ b)  # 00000110
print(a << b)  # 5 -> 10 -> 20 -> 40
print(40 >> b)  # 5
print(~a)  # 11111010 -> 00000110

# 멤버십 연산자
print("a" in "apple")
print(3 in [1, 2, 3])

# 삼항 연산자
# int max = a > b ? a : b;
max_num = a if a > b else b

# a값이 짝수면 "짝수", 홀수면 "홀수" 출력
a = int(input())

print("짝수" if a % 2 == 0 else "홀수")

score = 85

# 90점 이상이면 "A"
# 80점 이상이면 "B"
# 70점 이상이면 "C"
# 70점 미만이면 "D"

print("A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D")
