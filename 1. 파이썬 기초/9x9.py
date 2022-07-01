n= int(input('구구단 몇단을 계산할까요?'))
print(f'구구단 {n}단을 계산합니다.')
for i in range(1,10):
    print(f'{n} X {i} = {n*i}')