#FINAL INSERTION SORT!!!

import time
import random
import matplotlib.pyplot as plt


x = []
y = []

print("INSERTION SORT")
print("--To be sorted--")

z1 = int(input("No. of integers: "))
start_time = time.time()
ins1 = random.sample(range(0, z1), z1)

def insertion_sort1():
    for i in range(0, z1):
        value = ins1[i]
        pos = i
        while pos > 0 and ins1[pos - 1] > value:
            ins1[pos] = ins1[pos - 1]
            pos = pos - 1

        ins1[pos] = value

    print(ins1)
    x.append(z1)

end_time = time.time()
runTime1 = end_time - start_time
print("Execution time:", runTime1)

insertion_sort1()

z2 = int(input("No. of integers: "))
start_time = time.time()
ins2 = random.sample(range(0, z2), z2)

def insertion_sort2():
    for i in range(1, z2):
        value = ins2[i]
        pos = i
        while pos > 0 and ins2[pos - 1] > value:
            ins2[pos] = ins2[pos - 1]
            pos = pos - 1

        ins2[pos] = value

    print(ins2)
    x.append(z2)

end_time = time.time()
runTime2 = end_time - start_time
print("Execution time:", runTime2)

insertion_sort2()

z3 = int(input("No. of integers: "))
start_time = time.time()
ins3 = random.sample(range(0, z3), z3)

def insertion_sort3():
    for i in range(1, z3):
        value = ins3[i]
        pos = i
        while pos > 0 and ins3[pos - 1] > value:
            ins3[pos] = ins3[pos - 1]
            pos = pos - 1

        ins3[pos] = value

    print(ins3)
    x.append(z3)

end_time = time.time()
runTime3 = end_time - start_time
print("Execution time:", runTime3)


insertion_sort3()

z4 = int(input("No. of integers: "))
start_time = time.time()
ins4 = random.sample(range(0, z4), z4)

def insertion_sort4():
    for i in range(1, z4):
        value = ins4[i]
        pos = i
        while pos > 0 and ins4[pos - 1] > value:
            ins4[pos] = ins4[pos - 1]
            pos = pos - 1

        ins4[pos] = value

    print(ins4)
    x.append(z4)

end_time = time.time()
runTime4 = end_time - start_time
print("Execution time:", runTime4)

insertion_sort4()

z5 = int(input("No. of integers: "))
start_time = time.time()
ins5 = random.sample(range(0, z5), z5)

def insertion_sort5():
    for i in range(1, z5):
        value = ins5[i]
        pos = i
        while pos > 0 and ins5[pos - 1] > value:
            ins5[pos] = ins5[pos - 1]
            pos = pos - 1

        ins5[pos] = value

    print(ins5)
    x.append(z5)

end_time = time.time()
runTime5 = end_time - start_time
print("Execution time:", runTime5)

insertion_sort5()


left = [1, 2, 3, 4, 5]
height = [runTime1, runTime2, runTime3, runTime4, runTime5]

tick_label = [z1, z2, z3, z4, z5]

plt.bar(left, height, tick_label=tick_label,
        width=0.5, color=['green'])

plt.xlabel('Number of Integers')
plt.ylabel('Execution Time (sec)')

plt.title("Insertion Sort")
plt.show()
