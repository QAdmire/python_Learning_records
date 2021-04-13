# 请在## Begin ##和## End ##间补充代码
import math
a=float(input("请输入系数a:"))
b=float(input("请输入系数b:"))
c=float(input("请输入系数c:"))x=int(input())

for 
if (a == 0):
    if (b == 0):print("此方程无解！")
    else:print(str.format("此方程的解为:{0:.3f}", -c / b))
else:
########## Begin ##########
    if b**2-4*a*c == 0:
        print("此方程有两个相等实根:{:.3f}".format(-b/(2*a)))
    elif b**2-4*a*c > 0:
        print("此方程有两个不等实根:{0:.3f}和{1:.3f}".format(-b/(2*a)+pow(b**2-(4*a*c),1/2)/(2*a),-b/(2*a)-pow(b**2-(4*a*c),1/2)/(2*a)))
    else:
        x = pow(b**2-(4*a*c),1/2)/(2*a)
        print("此方程有两个不等虚根:{0:.3f}+{1:.3f}i和{0:.3f}-{1:.3f}i".format(-b/(2*a),x.imag))
########## End ##########