import math

print("введите коэффициент для уравнения")
print("ax^2+ bx + c = 0:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

discr = b ** 2-4 * a * c
print("дискриминант D = %.2f" % discr)

if discr > 0:
    x1 = (-b + math.sqrt(discr)) / (2*a)
    x2 = (-b + math.sqrt(discr)) / (2 * a)
    print("x1 = %.2f /nx2 = % (2*a")
elif discr == 0:
    x = -b / (2*a)
    print("x = %.2f" % x)
else:
    print("корней нет")
    

