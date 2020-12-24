import matplotlib.pyplot as plt


def collatz(n):
    l = [n]
    while n != 1:
        if n % 2 == 0:
            n = n/2
            l.append(n)
        else:
            n = n*3 + 1
            l.append(n)
    return l


initial = int(input("Enter an integer n: "))
sequence = collatz(initial)

plt.style.use("ggplot")

plt.plot(sequence)
plt.ylabel("Number step")
plt.xlabel("Iteration")
plt.tight_layout()
plt.show()
