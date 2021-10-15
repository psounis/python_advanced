from enum import IntFlag


class Perm(IntFlag):
    READ = 1
    WRITE = 2
    EXECUTE = 4

RW = Perm.READ | Perm.WRITE
print(Perm.READ in RW)

RWX = RW | Perm.EXECUTE
print(RWX)

RX = RWX & ~ Perm.WRITE
print(RX)