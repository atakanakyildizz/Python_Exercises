# [2.2] The Drunkard’s Walk
import math
import random


def main():
    # if he turns left x = x+1
    # if he turns right x = x-1
    # if he goes ahaed y = y+1
    # if he turns back y = y-1
    print(f"Drunkard's initial point is (0,0)")
    x, y = 0, 0
    for i in range(100):
        x = x + random.choice([-1, 1])
        y = y + random.choice([-1, 1])

    distance = math.sqrt((x**2)+(y**2))
    print(f"Drunkard's initial point is ({x},{y})\n)"
          f"Distance between this points is {distance}")


if __name__ == '__main__':
    main()
