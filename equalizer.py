import time
import math

θ_1 = θ_2 = θ_3 = θ_4 = 0
W = 40


def up(nline=1):
    #          ↓ interested? just search for 'escape sequence'
    print(f"\x1b[{nline}A", end="")


def bar(value):
    π = math.pi
    n = int(W * (math.sin(π*value/180) + 1))
    print("#"*n + " "*(2*W-n))


while True:
    θ_1 += 15
    bar(θ_1)
    θ_2 += 31
    bar(θ_2)
    θ_3 += 11
    bar(θ_3)
    θ_4 += 9
    bar(θ_4)
    time.sleep(0.1)
    up(4)

# vim: sw=4 ts=4 expandtab
