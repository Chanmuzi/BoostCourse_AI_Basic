while True:
    print('구구단 몇 단을 계산할까요(1~9)?')

    n = int(input())
    if 1 <= n and n < 10:
        print(f'구구단 {n}단을 계산합니다.')
        for i in range(1,10):
            print(f'{n} X {i} = {n*i}')
    else: 
        print('구구단 게임을 종료합니다')
        break