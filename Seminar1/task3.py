# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.



a = int(input("Введите количество учеников в классе 1: "))
b = int(input("Введите количество учеников в классе 2: "))
c = int(input("Введите количество учеников в классе 3: "))

people = a+b+c
desks = -(-people//2)

print("Количетсво парт: ", desks)