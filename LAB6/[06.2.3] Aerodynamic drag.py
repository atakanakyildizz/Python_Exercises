# [06.2.3] Aerodynamic drag

ro, A, CD = 1.23, 2.5, 0.2
v = int(input("Enter the car's speed: "))
FD = 1 / 2 * ro * (v ** 2) * A * CD
P = FD * v
Hp = P/745.7
print(f"The power is {P}\n"
      f"Horsepower is {Hp}")
