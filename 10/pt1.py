from math import inf


lines = [x.strip().split() for x in open("input.txt").readlines()]


def buttonXor(state, button):
    return tuple(state[i] ^ (i in button) for i in range(len(state)))

ret = 0

for line in lines:
    endState = tuple(int(x == '#') for x in line[0][1:-1])

    buttons = line[1:-1]
    buttons = [{int(y) for y in x[1:-1].split(',')} for x in buttons]
    
    states = {(0,) * len(endState) : 0}
    
    for button in buttons:
        for s, n in states.copy().items():
            press = buttonXor(s, button)
            states[press] = min(states.get(press, inf), n+1)
    
    ret += states[endState]

print(ret)