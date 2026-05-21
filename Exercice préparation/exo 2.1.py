import matplotlib.pyplot as plt

def u(n):
    return n**2 - 3

for n in range(0, 100, 3):   # pas de 3
    print(u(n))
    plt.plot(n, u(n), '*r')

plt.show()

##pip install matplotlib  pour faire marcher
