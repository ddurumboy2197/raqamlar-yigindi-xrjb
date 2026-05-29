def raqamlar_yigindi(son):
    yigindi = 0
    for raqam in str(son):
        yigindi += int(raqam)
    return yigindi

son = int(input("Sonni kiriting: "))
print(raqamlar_yigindi(son))
