import time

W = 40
for i in range(W):
    for j in range(W-i):
        print(" "*j + "#", end="\r")
        time.sleep(0.01)

print()

# vim: sw=4 ts=4 expandtab
