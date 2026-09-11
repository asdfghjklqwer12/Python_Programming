# 튜플 심화

# ===========================================================
#  튜플에서 제공하는 메소드
# ===========================================================

t = (1, 1, 2, 2, 2)

print(t.count(1))  # 1이 몇개 있는지?

print(t.index(2))  # 2의 첫번째 인덱스는?


# ===========================================================
#  그 외
# ===========================================================

# tuple -> list 변환
l = list(t)
print(l)

# list -> tuple 변환
t = tuple(l)
print(t)

# 튜플을 이용해서 swap하기
a, b = 10, 20
a, b = b, a
print(a, b)

# 튜플 언패킹
t = (1, 2, 3, 4)

print(*t)

a, b, c, d = t
print(a, b, c, d)

a, *b, c = t
print(a, b, c)

t2 = (5, 6)
print((*t, *t2))

# zip 함수 사용
subjects = ("국어", "수학", "영어")
scores = (80, 90, 95)

# (('국어', 80), ('수학', 90), ('영어', 95)) 출력하기
for (
    i,
    j,
) in zip(subjects, scores):
    print(f"({i}, {j})", end=" ")
print()
# 걍 튜플하고 집으로 감싸면 나옴

# ===========================================================
#  Tuple Comprehension은 없음
# ===========================================================

# Generator 표현식
gen = (x for x in range(1, 11))
print(gen)

print(next(gen))
print(next(gen))
print(next(gen))

for i in gen:
    print(i, end=" ")
print()

a = [x for x in range(1, 11)]
b = (x for x in range(1, 11))

print(sum(a), sum(a))
print(sum(b), sum(b))


# 1 ~ 10의 제곱수 튜플 만들기
# ()는 튜플이 아니라 generator를 생성하는 generator 표현식임
result = tuple((x**2 for x in range(1, 11)))
print(result)

# tuple의 생성자에 generator를 넘겨 값을 순회하면서 튜플을 만듦


# 두 점의 x, y, z축 좌표값끼리 더한 튜플을 만들기
p1 = (1, 2, 3)
p2 = (10, 20, 30)

result = tuple(a + b for a, b in zip(p1, p2))
print(result)

# =========================================================
#  🔥 실습 문제
# =========================================================

# 일주일 동안의 학습 시간을 저장한 튜플
days = ("일", "월", "화", "수", "목", "금", "토")
hours = (2, 3, 1, 4, 5, 2, 6)

# 1️⃣ 월 ~ 금까지 총 학습시간 출력하기
print(sum(hours[1:-1]))  # ✅ 15시간


# 2️⃣ 가장 많이 공부한 시간 출력하기
print(max(hours))  # ✅ 6시간


# 3️⃣ 가장 많이 공부한 요일 출력하기
result = hours.index(max(hours))
print(days[result])  # ✅ 토요일

# hours, days = max(zip(hours, days))
# print(days)

# 4️⃣ 가장 높은 점수와 가장 낮은 점수 출력하기
scores = (90, 85, 78, 92, 88, 76)

print(sorted(scores)[-1], sorted(scores)[0])
print(max(scores), min(scores))  # ✅ max 점수: 92점, min 점수: 76점


# 5️⃣ 과일가게 총 재고 금액 구하기
stocks = (
    ("사과", 1000, 5),
    ("바나나", 2000, 3),
    ("체리", 5000, 2),
)

# 총 재고 금액 출력
# ✅ 총액: 21,000원
result = tuple(zip(*stocks))[1:]
x, y = result
asdf = 0

for i in range(3):
    asdf += x[i] * y[i]
print(asdf)

total = sum(i[1] * i[2] for i in stocks)
print(total)

total = sum(price * qty for _, price, qty in stocks)
print(total)

stocks = (("사과, 바나나, 체리"), (1000, 2000, 5000), (5, 3, 2))

total = sum((y * z for x, y, z in zip(*stocks)))
print(total)
