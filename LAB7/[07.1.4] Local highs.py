#[07.1.4] Local highs

my_list = [2,33,6,74,7,24]

def local_maksima(list):
    a = list[0]
    counter =0
    for i in range(len(list)):
        if a < list[i]:
            a = list[i]
        elif a == list[i]:
            counter += 1
    if counter > 1:
        print("There is no local maxima")
    else:
        return a

print(f"Local max is = {local_maksima(my_list)}")