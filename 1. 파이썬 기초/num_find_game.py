import random

num = random.randint(1,101)

userNum = int(input('숫자를 맞춰보세요 (1~100): '))
while userNum != num:
    if userNum > num:
        userNum = int(input('숫자가 너무 큽니다'))
    else: userNum = int(input('숫자가 너무 작습니다'))
print(f'정답입니다. 입력한 숫자는 {num}입니다')