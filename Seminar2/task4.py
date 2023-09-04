# Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи. Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел, записанных на новой строчке каждое. Здесь каждое число – это масса соответствующего арбуза

data = [int(i) for i in input("Введите данные по арбузам: ").split()]

m1 = data[0]
m2 = data[0]

for mel in data: 
    if mel > m1:
        m1 = mel
    elif mel < m2:
        m2 = mel


print(f"Самый большой арбуз {m1}, самый маленький арбуз {m2}")