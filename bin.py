import time

W = 20
counter = 1

while True:
    # result of bin() has format like '0b....',
    # so first 2 characters must die.
    print(bin(counter)[2:].replace('0', " ")
                          .replace('1', "#")
                          # .rjust(W)  # if you want to align right :)
                          , end="\r")
    counter += 1
    time.sleep(0.05)

# vim: sw=4 ts=4 expandtab
