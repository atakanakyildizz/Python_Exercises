#[07.1.6] Ordered list

import random

a = []
for i in range(20):
    a.append(random.randint(0,99))
    a = sorted(a)
print(a)