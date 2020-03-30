'''
    Juan Melendres

    Install:

     * pip install pyobjc
     * pip install playsound

    Run:
    
    python3 melody_generator.py
'''

import random
from datetime import datetime
import playsound as ps

notes = [
    "sound/do.m4a", "sound/re.m4a", "sound/mi.m4a",
    "sound/fa.m4a", "sound/sol.m4a", "sound/la.m4a",
    "sound/si.m4a"
        ]

rangeMatrix = []
probMatrix = []
sequence = []

random.seed(datetime.now())

do = "do"
re = "re"
mi = "mi"
fa = "fa"
sol = "sol"
la = "la"
si = "si"
octave = [do, re, mi, fa, sol, la, si]

def stochasticMatrix():
    # generate chances of transition
    # matrix[len(octave)][len]
    # 20 notas
    # sound
    for _ in range(len(octave)):
        ranges = []
        probs = []
        maxProb = 100
        testCurr = 0
        currProb = 0
        r1 = 0
        for i in range(len(octave)):
            r1 = random.randint(0, maxProb)
            if(i == len(octave) - 1):  # Reached final element
                r1 = maxProb  # Last element should make sure of sum 1 total prob
            maxProb -= r1
            ranges.append(r1)
            currProb += r1

            r1 /= 100
            testCurr += r1
            probs.append(r1)

        rangeMatrix.append(ranges)
        probMatrix.append(probs)
    print('\n'.join(['  '.join(['{:4}'.format(item) for item in row]) for row in probMatrix]))
    print("")

def transition(current):
    nextState = random.randint(0,100)
    distance = 0

    for i in range (len(rangeMatrix[current])):
        distance += rangeMatrix[current][i]
        if(nextState <= distance):
            sequence.append(i)
            print(octave[i], " ", end = '')
            break
    return i
        
def main():
    stochasticMatrix()
    start = 0
    print(octave[start], " ", end = '')
    sequence.append(start)
    
    n = 20
    for i in range (n):
        start = transition(start)
    print("")
    
    for i in sequence:
        ps.playsound(notes[i])

main()
