import matplotlib.pyplot as plt

def u(n):
    return n**2 - 3

# range(0, 100, 3) : de 0 à 99, avec un pas de 3
# donc n prend les valeurs : 0, 3, 6, 9, ..., 99
for n in range(0, 100, 3):
    print(u(n))
    plt.plot(n, u(n), 'r')  # 'r' = rouge, place un point

##pip install matplotlib  pour faire marcher
