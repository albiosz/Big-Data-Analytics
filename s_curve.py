import numpy as np
import matplotlib.pyplot as plt
#task 1 & 2
r = 2
b = 3

#task 3
param = 2

def and_construction(p, r):
    return pow(p,b)

def or_construction(p, b):
    return 1-pow(1-p, b)

def task_one(p1, p2, r, b):
    result_p1 = and_construction(p1, r)
    result_p1 = or_construction(result_p1, b)
    result_p2 = and_construction(p2, r)
    result_p2 = or_construction(result_p2, b)
    return(result_p1, result_p2)

def task_two(p1 ,p2 , r, b):
    result_p1 = or_construction(p1, b)
    result_p1 = and_construction(result_p1, r)
    result_p2 = or_construction(p2, b)
    result_p2 = and_construction(result_p2, r)
    return(result_p1, result_p2)

def task_3(p1, p2, r, b):
    result_p1 = and_construction(p1, r)
    result_p1 = or_construction(result_p1, b)
    result_p1 = and_construction(result_p1, r)
    result_p2 = and_construction(p2, r)
    result_p2 = or_construction(result_p2, b)
    result_p2 = and_construction(result_p2, r)
    return(result_p1, result_p2)

def task_4(p1, p2, r, b):
    result_p1 = or_construction(p1, b)
    result_p1 = and_construction(result_p1, r)
    result_p1 = or_construction(result_p1, b)
    result_p1 = and_construction(result_p1, r)
    result_p2 = or_construction(p2, b)
    result_p2 = and_construction(result_p2, r)
    result_p2 = or_construction(result_p2, b)
    result_p2 = and_construction(result_p2, r)
    return(result_p1, result_p2)


def main():
    d1 = 0.3
    d2 = 0.6
    p1 = 1 - d1
    p2 = 1 - d2
    task1_list = []
    task2_list = []
    task3_list = []
    task4_list = []
    for p in np.linspace(0.1, 0.9, 8):
        probability = task_one(p, p, 2, 3)
        task1_list.append([probability[0]])
        probability = task_two(p, p, 3, 2)
        task2_list.append([probability[0]])
        probability = task_3(p, p, 2, 2)
        task3_list.append([probability[0]])
        probability = task_4(p, p, 2, 2)
        task4_list.append([probability[0]])
    print(task1_list)
    plt.ylim(0, 1)
    #plt.xlim(0, d1)
    plt.plot(task1_list)
    plt.show()
    plt.plot(task2_list)
    plt.show()
    plt.plot(task3_list)
    plt.show()
    plt.plot(task4_list)
    plt.show()


if __name__ == "__main__":
    main()