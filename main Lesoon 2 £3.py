
print("Введите координаты  и радиус круга")
x = float(input('x: = '))
y = float(input('y: = '))
r = float(input('r: = '))
import  math
hypot = math.sqrt(x ** 2 + y ** 2)


if hypot <= r:
    print("Точка принадлежит кругу")
else:
    print("Точка не принадлежит кругу")


