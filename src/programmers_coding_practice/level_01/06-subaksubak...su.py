'''
:reference: https://programmers.co.kr/learn/courses/30/lessons/12922?language=python3
'''

def solution_01(n):
    
    rsl = ''
    for i in range(1, n + 1):
        rsl += '수' if i % 2 else '박'
        
    return rsl


def solution_02(n):
    
    return ''.join('수박'[i % 2] for i in range(0, n))


def main(n):
    print(solution_01(n))
    print(solution_02(n))



if __name__ == '__main__':
    N = 3
    
    main(N)
    