# [06.1.1] Vowel Count

def count_vowels(string):
    counter = 0
    for i in range(len(string)):
        if string[i].lower() == 'a' or 'e' or 'i' or 'o' or 'u':
            counter += 1
    return counter


def main():
    print(count_vowels("AAsdfaadfaaasfd"))


if __name__ == "__main__":
    main()
