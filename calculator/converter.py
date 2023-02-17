from bases import Bases
bases = Bases()

def from_base(num, base):
    bases = Bases()
    try:
        if base == 2:
            return bases.fromBase2(str(num))
        elif base == 10:
            return int(num)
        elif base == 16:
            return bases.fromBase16(str(num))
        elif base == 36:
            return bases.fromBase36(str(num))
        elif base == 62:
            return bases.fromBase62(str(num))
    except ValueError as e:
        print(f"Invalid input. The input number is not valid in the given base.")
        exit()

def to_base(num, base):
    bases = Bases()
    try:
        if base == 2:
            return bases.toBase2(num)
        elif base == 10:
            return num
        elif base == 16:
            return bases.toBase16(num)
        elif base == 36:
            return bases.toBase36(num)
        elif base == 62:
            return bases.fromBase62(num)
    except TypeError:
        print(f"Invalid input. The input number is not valid in the given base.")
        exit()