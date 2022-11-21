#[07.1.5] The same elements

my_first_list = [1,4,9,16,9,7,4,9,11]
my_second_list = [11,11,7,9,16,4,1]

def same_set(a,b):
    a = list(dict.fromkeys(a))
    b = list(dict.fromkeys(b))
    a = (sorted(a))
    b = (sorted(b))

    counter = 0
    if len(a) > len(b):
        for i in range(len(a)):
            if a[i] == b[i]:
                counter = counter+1
        if counter == len(a):
            return True
        else:
            return False
    else:
        for i in range(len(b)):
            if a[i] == b[i]:
                counter = counter +1
        if counter == len(b):
            return True
        else:
            return False

print(same_set(my_first_list,my_second_list))