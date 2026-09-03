# 반복분 : while문, for문

# while문
# 1 ~ 10까지 반복 출력
i = 1
while i <= 10:
    print(i)
    i += 1
else:
    print("End")

nums = [1, 3, 5, 7, 9]
target = 2
a = 0

while a < len(nums):
    if nums[a] == target:
        print(str(target) + " found")
        break
    a += 1
else:
    print(str(target) + " not found")

# 1 ~ 10 까지의 합
i = 1
tot = 0

while i <= 10:
    if i % 2 == 0:
        tot += i
    i += 1

print(tot)
