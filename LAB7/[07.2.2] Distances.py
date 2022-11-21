# [07.2.2] Distances

space_number = int(input('Enter the number of space: '))


parking_slot = []

for i in range(space_number):
    parking_slot.append("_")


for i in range(space_number):
    if int(space_number/2) == i:
        parking_slot[i] = "x"

print(f"First situation: \n{parking_slot}")
counter=0
counter2 = 0

while parking_slot[counter] == "_":
    counter = counter + 1

while parking_slot[counter+1] == "_":
    counter2 = counter2 + 1
    if counter+counter2 + 1== space_number:
        break

if counter > counter2:
    for i in range(counter):
        if int(counter / 2) == i:
            parking_slot[i] = "x"
else:
    for i in range(counter2):
        if int(counter2 / 2) == i:
            parking_slot[i] = 'x'

print(f"Second situation: \n{parking_slot}")