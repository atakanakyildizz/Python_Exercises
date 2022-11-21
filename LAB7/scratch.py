#[07.1.2] List of random numbers
import random

Repatation = 10
randomNumberList = []

while len(randomNumberList) != Repatation:
    a = random.randint(1,100)
    if a % 2 == 0 :
        if a / 10 > 9:
            if a/10 % 2 == 0:
                randomNumberList.append(a)
        else:
            randomNumberList.append(a)

print(randomNumberList)


