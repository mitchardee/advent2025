from functools import cache


lines = [x.strip().split() for x in open("input.txt").readlines()]

ret = 0
for line in lines[30:]:
    a = line[0][:-1].split('x')
    area = int(a[0]) * int(a[1])
    
    blocks = sum(int(x) for x in line[1:])
    
    ret += blocks * 9 <= area



print(ret)