# [1.1] Out-of-range

def main():
    sequence = [20]
    try:
        for i in range(len(sequence)+1):
            print(sequence[i])
    except IndexError:
        print(f'You have a problem ')
if __name__ == '__main__':
    main()
