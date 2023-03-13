from cmath import sin

def blood_type(number):
    if number == 1:
        print("Может отдавать кровь группам I, II, III, IV. Может принимать кровь у I группы.")
    elif number == 2:
        print("Может отдавать кровь группам II, IV. Может принимать кровь у I и II группы.")
    elif number == 3:
        print("Может отдавать кровь группам III, IV. Может принимать кровь у I и III группы.")
    else:
        print("Может отдавать кровь группе IV. Может принимать кровь у I, II, III, IV группы.")

blood_number = int(input("Введите группу крови: "))
blood_type(blood_number)

def size_eye(f, h, a):
    L = f / 3 + h / sin(a)
    return L

f = int(input("Введите ширину канала: "))
h = int(input("Введите толщину роговицы: "))
a = int(input("Введите угол, под которым осуществляется вход инструмента хирурга: "))

L = size_eye(f, h, a)
print("Длина разреза канала = ", L)