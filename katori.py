import time
import math

W = 30
HALF = W//2


# some sort of linear algebraic discriminant,
#  sin, cos, blah, blah, blah...
def it_is_on_the_line(x,y):
    r = (x*x + y*y + t*3)/W/W*t/10
    cs, sn = math.cos(r), math.sin(r)
    tx, ty = int(x * cs - y * sn), int(x * sn + y * cs) 
    return  tx < 0


def up(nline=1):
    print(f"\x1b[{nline}A", end="")


t = 0
while True:
    t += 1
    for y in range(-HALF, HALF):
        line = ""   # reset buffer for a line
        for x in range(-HALF, HALF):
            if it_is_on_the_line(x,y):
                line += "#"
            else:
                line += " "
        print(line)   # output just a line
    time.sleep(0.05)
    up(W)

# vim: sw=4 ts=4 expandtab
