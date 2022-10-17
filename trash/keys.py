import random

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "0123456789"
special = "!@#$%^&*()-+"

for x in range(1):
    from time import sleep
    sleep(1)
    ans = lower_case + upper_case + num + special
    length = 64
    password = "".join(random.sample(ans, length))
    print(password)


y = (0.1+0.2)/1
print(y)
# output
# 0.30000000000000004
