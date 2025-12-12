from collections import defaultdict
from functools import cache
from math import inf


lines = [x.strip().split() for x in open("input.txt").readlines()]


def buttonAdd(state, button):
    return tuple(state[i] + (i in button) for i in range(len(state)))

#Divide by two since that's the next step each time we subtract
#Only works for states of same parity
def stateSubtract(s1, s2):
    return tuple((s1[i] - s2[i]) // 2 for i in range(len(s1)))

def stateParity(s):
    return tuple(x % 2 for x in s)


ret = 0

for line in lines:
    endState = tuple(int(x) for x in line[-1][1:-1].split(','))

    buttons = line[1:-1]
    buttons = [{int(y) for y in x[1:-1].split(',')} for x in buttons]

    startState = (0,) * len(endState)
    presses = 0

    states = {startState : 0}
    
    for button in buttons:
        for s, n in states.copy().items():
            press = buttonAdd(s, button)
            states[press] = min(states.get(press, inf), n+1)
    
    #Make a dict with every combination of presses keyed by the parity of the result
    parityStates = defaultdict(list)
    for s, n in states.items():
        parityStates[stateParity(s)].append((s, n))
    
    @cache
    def rec(state):
        #Base case, no buttons to press
        if not any(state):
            return 0
        #Negative means we've pressed something too many times
        if any(x < 0 for x in state):
            return inf
        
        return min((n + 2 * rec(stateSubtract(state, s)) for s, n in parityStates[stateParity(state)]), default=inf)
    
    ret += rec(endState)

print(ret)