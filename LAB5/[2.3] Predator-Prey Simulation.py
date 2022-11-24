# [2.3] Predator-Prey Simulation

def main():
    A, B, C, D = 0.1, 0.01, 0.01, 0.00002
    x0, y0 = 1000, 20
    for i in range(100):
        x1 = x0 * (1 + A - B * y0)
        y1 = y0 * (1 - C + D * x0)
        x0, y0 = x1, y1
        print(int(x1), int(y1))


if __name__ == '__main__':
    main()
