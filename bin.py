import time

W = 10

for counter in range(1, 2**W):
    # result of bin() has format like '0b....',
    # so first 2 characters must die.
    print(bin(counter)[2:].replace('0', " ")
                          .replace('1', "#")
                          # .rjust(W)  # if you want to align right :)
                          , end="\r")
    time.sleep(0.05)

print()

# vim: sw=4 ts=4 expandtab
