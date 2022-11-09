print("--------------------------------------------------------------")
print("I can solve cubics with 3 real root i.e. ax^3+bx^2+cx+d=0.")
print("--------------------------------------------------------------")

name = input("What's your name?")

a = int(input("What is your a?"))
b = int(input("What is your b?"))
c = int(input("What is your c?"))
d = int(input("What is your d?"))

def f(a , b , c , d) :
    m1 = (-b ** 3) / (27 * (a ** 3)) + (b * c) / (6 * (a ** 2)) - d / 2 / a
    m2 = c / (3 * a) - (b ** 2) / (9 * (a ** 2))
    m3 = (m1 + (m1 ** 2 + m2 ** 3) ** 0.5) ** (1 / 3)
    m4 = (m1 - (m1 ** 2 + m2 ** 3) ** 0.5) ** (1 / 3)
    x = m3 + m4 - b / 3 / a
    return x.real

cubic = str(a) + "x^3+" + str(b) + "x^2+" + str(c) + "x+" + str(d) + "=0"
cubic = cubic.replace("0x^3", "")
cubic = cubic.replace("+0x^2", "")
cubic = cubic.replace("+0x^1", "")
cubic = cubic.replace("+0", "")
cubic = cubic.replace("+-", "-")
cubic = cubic.replace("1x^3", "x^3")
cubic = cubic.replace("1x^2", "x^2")
cubic = cubic.replace("1x^1", "x^1")

print("Hello" , name , end = "")
print(", I will solve" , cubic , end = "")
print(".")
print("The root of the cubic is" , f(a , b , c , d))

quit()