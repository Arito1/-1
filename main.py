a=int(input("a = "))
b=int(input("b = "))
c=int(input("c = "))
if a + b <= c or a + c <= b or c + b <= a:
    print("ТАКОГО ТРЕУГОЛЬНИКА НЕ СУЩЕСТВУЕТ")
elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or c**2 + b**2 == a**2:
    print("ТРЕУГОЛЬНИК ПРЯМОУГОЛЬНЫЙ")
elif a==b==c:
    print("ТРЕУГОЛЬНИК РАВНОСТОРОНИЙ")
elif a==b or a==c or b==c:
    print("ТРЕУГОЛЬНИК РАВНОБЕДРЕННЫЙ")
elif a!=b and b!=c and c!=a:
    print("ТРЕУГОЛЬНИК ПРОИЗВОЛЬНЫЙ")