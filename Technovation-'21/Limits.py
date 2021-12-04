Req = 125
Ro = 300
V = 5

def Rx(x):
    return 2*Ro*x

def R0(x):
    return Req - Rx(x)

def V(x):
    return (Rx(x) * V)/Req

print("i Rx  R0  V")
for i in range(10):
    print(i)