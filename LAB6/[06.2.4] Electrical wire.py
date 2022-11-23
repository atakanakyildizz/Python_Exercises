# [06.2.4] Electrical wire
import math


def diameter(wire_gauge):
    return 0.127 * (92 ** ((26 - wire_gauge) / 39))


def copper_wire_resistance(length, wire_gauge):
    ro = 1.678 * (10 ** -8)
    a = math.pi * (wire_gauge ** 2) / 4
    r = ro * length / a
    return r


def aluminum_wire_resistance(length, wire_gauge):
    ro = 2.82 * 10**-8
    a = math.pi * (wire_gauge ** 2) / 4
    r = ro * length / a
    return r


def main():
    lengt = int(input("Enter the length: "))
    wire_gauge = int(input("Enter the wire gauge: "))
    print(f"diameter = {diameter(wire_gauge)}\n"
          f"copper wire resistance = {copper_wire_resistance(lengt,wire_gauge)}\n"
          f"aluminum wire resistance = {aluminum_wire_resistance(lengt,wire_gauge)}")


if __name__ == "__main__":
    main()
