# [06.1.3] Geometric solids
import math


def sphere_volume(r):
    return math.pi*4*(r**3)/3


def sphere_surface(r):
    return math.pi*4*(r**2)


def cylinder_volume(r, h):
    return math.pi * (r**2) * h


def cylinder_surface(r, h):
    return 2 * math.pi * r * (r+h)


def cone_volume(r, h):
    return math.pi*(r**2)*h/3


def cone_surface(r, h):
    return math.pi*r*(r+math.sqrt((h**2)+(r**2)))


def main():
    r = int(input("Enter the radius: "))
    h = int(input("Enther the height: "))
    print(f"sphere volume: {sphere_volume(r)}\n"
          f"sphere surface: {sphere_surface(r)}\n"
          f"cylinder volume: {cylinder_volume(r, h)}\n"
          f"cylinder surface: {cylinder_surface(r, h)}\n"
          f"cone volume: {cone_volume(r, h)}\n"
          f"cone surface: {cone_surface(r, h)}")


if __name__ == "__main__":
    main()
