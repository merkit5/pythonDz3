import math
import cmath
a = float(input("Введите первый коэффицент: "))
b = float(input("Введите второй коэффицент: "))
c = float(input("Введите третий коэффицент: "))
D = b**2 - 4*a*c
print("Дискрименант квадратного уравнения: ", D)
if D < 0:
    x1 = (-b + D ** 0.5) / (2 * a)
    x2 = (-b - D ** 0.5) / (2 * a)
    print('x₁ = ' + str(x1))
    print('x₂ = ' + str(x2))
if D > 0:
    x1 = ((-b-math.sqrt(D))/(2*a))
    x2 = ((-b+math.sqrt(D))/(2*a))
    print("Корни квадратного уравнения: ", x1, ",", x2)
elif D == 0 :
    x1 = (-b / (2 * a))
    print("Корень квадратного уравнения: ", x1)
