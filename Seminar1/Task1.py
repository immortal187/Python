import random
proizv = int(input('Введите произведение чисел: '))
x = 0
y= 0
sum_pk = 0
proizv_pk = 0
while sum_pk != sum and proizv_pk != proizv:    
x = random.randint(0, 1000)
    y = random.randint(0, 1000)    
sum_pk = x + y
    proizv_pk = x * y
print('Вы загадали числа ', x, ' и ', y)