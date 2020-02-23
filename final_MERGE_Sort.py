import random
import time
import matplotlib.pyplot as plt



print("To be sorted...")


print("  ")
m1list = []
z1 = int(input("No. of integers: "))
for i in range(0, z1):
    m1st = random.randint(0, z1)
    m1list.append(m1st)
starttimem1 = time.time()


def Merge1(m1list):

    if len(m1list) > 1:
        mid = len(m1list) // 2
        array1 = m1list[:mid]
        array2 = m1list[mid:]
        Merge1(array1)
        Merge1(array2)
        i = 0
        j = 0
        k = 0
        while i < len(array1) and j < len(array2):
            if array1[i] <= array2[j]:
                m1list[k] = array1[i]
                i = i + 1
            else:
                m1list[k] = array2[j]
                j = j + 1
            k = k + 1
        while i < len(array1):
            m1list[k] = array1[i]
            i = i + 1
            k = k + 1
        while j < len(array2):
            m1list[k] = array2[j]
            j = j + 1
            k = k + 1


Merge1(m1list)
endtime1 = time.time()
m1 = endtime1 - starttimem1
print(m1list)
print('Execution Time: ', m1)
print("")

print("----")
m2list = []
z2 = int(input("No. of integers: "))
for i in range(0, z2):
    m2nd = random.randint(0, z2)
    m2list.append(m2nd)
starttimem2 = time.time()


def Merge2(m2list):
    if len(m2list) > 1:
        mid = len(m2list) // 2
        array1 = m2list[:mid]
        array2 = m2list[mid:]
        Merge2(array1)
        Merge2(array2)
        i = 0
        j = 0
        k = 0
        while i < len(array1) and j < len(array2):
            if array1[i] <= array2[j]:
                m2list[k] = array1[i]
                i = i + 1
            else:
                m2list[k] = array2[j]
                j = j + 1
            k = k + 1
        while i < len(array1):
            m2list[k] = array1[i]
            i = i + 1
            k = k + 1
        while j < len(array2):
            m2list[k] = array2[j]
            j = j + 1
            k = k + 1


Merge2(m2list)
endtime2 = time.time()
m2 = endtime2 - starttimem2
print(m2list)
print('Execution Time: ', m2)
print("")

print("----")
m3list = []
z3 = int(input("No. of integers: "))
for i in range(0, z3):
    m3rd = random.randint(0, z3)
    m3list.append(m3rd)
starttimem3 = time.time()


def Merge3(m3list):
    if len(m3list) > 1:
        mid = len(m3list) // 2
        array1 = m3list[:mid]
        array2 = m3list[mid:]
        Merge3(array1)
        Merge3(array2)
        i = 0
        j = 0
        k = 0
        while i < len(array1) and j < len(array2):
            if array1[i] <= array2[j]:
                m3list[k] = array1[i]
                i = i + 1
            else:
                m3list[k] = array2[j]
                j = j + 1
            k = k + 1
        while i < len(array1):
            m3list[k] = array1[i]
            i = i + 1
            k = k + 1
        while j < len(array2):
            m3list[k] = array2[j]
            j = j + 1
            k = k + 1


Merge3(m3list)
endtime3 = time.time()
m3 = endtime3 - starttimem3
print(m3list)
print('Execution Time: ', m3)
print("")

print("----")
m4list = []
z4 = int(input("No. of integers: "))
for i in range(0, z4):
    m4th = random.randint(0, z4)
    m4list.append(m4th)
starttimem4 = time.time()

def Merge4(m4list):
    if len(m4list) > 1:
        mid = len(m4list) // 2
        array1 = m4list[:mid]
        array2 = m4list[mid:]
        Merge4(array1)
        Merge4(array2)
        i = 0
        j = 0
        k = 0
        while i < len(array1) and j < len(array2):
            if array1[i] <= array2[j]:
                m4list[k] = array1[i]
                i = i + 1
            else:
                m4list[k] = array2[j]
                j = j + 1
            k = k + 1
        while i < len(array1):
            m4list[k] = array1[i]
            i = i + 1
            k = k + 1
        while j < len(array2):
            m4list[k] = array2[j]
            j = j + 1
            k = k + 1

Merge4(m4list)
endtime4 = time.time()
m4 = endtime4 - starttimem4
print(m4list)
print('Execution Time: ', m4)
print("")


print("----")
m5list = []
z5 = int(input("No. of integers: "))
for i in range(0, z5):
    m5th = random.randint(0, z5)
    m5list.append(m5th)
starttimem5 = time.time()

def Merge5(m5list):
    if len(m5list) > 1:
        mid = len(m5list) // 2
        array1 = m5list[:mid]
        array2 = m5list[mid:]
        Merge5(array1)
        Merge5(array2)
        i = 0
        j = 0
        k = 0
        while i < len(array1) and j < len(array2):
            if array1[i] <= array2[j]:
                m5list[k] = array1[i]
                i = i + 1
            else:
                m5list[k] = array2[j]
                j = j + 1
            k = k + 1
        while i < len(array1):
            m5list[k] = array1[i]
            i = i + 1
            k = k + 1
        while j < len(array2):
            m5list[k] = array2[j]
            j = j + 1
            k = k + 1

Merge5(m5list)
endtime5 = time.time()
m5 = endtime5 - starttimem5
print(m5list)
print('Execution Time: ', m5)
print("")


left = [1, 2, 3, 4, 5]
height = [m1, m2, m3, m4, m5]

tick_label = [z1, z2, z3, z4, z5]

plt.bar(left, height, tick_label=tick_label,
        width=0.5, color=['green'])

plt.xlabel('Number of Integers')
plt.ylabel('Execution Time (sec)')

plt.title('Merge Sort')

plt.show()
