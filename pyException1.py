# Реализуйте метод, принимающий в качестве аргументов два целочисленных массива, и возвращающий новый массив,
# каждый элемент которого равен разности элементов двух входящих массивов в той же ячейке. Если длины массивов не равны,
# необходимо как-то оповестить пользователя.

def devision_arr(arr1, arr2):
    arr3 = []
    for i in range(len(arr1)):
        arr3.append(int(arr1[i]) / int(arr2[i]))
    return arr3


def arrays_check(arr1, arr2):
    if (len(arr2) == 0 or len(arr1) == 0):
        return -1
    elif (len(arr2) != len(arr1)):
        return -2
    elif (check_array(arr2) or check_array(arr1)):
        return -3


def catch_exception(a):
    if a == -1:
        return 'Массив пуст'
    elif a == -2:
        return 'Длины массивов разные'
    elif a == -3:
        return 'Какой то из элементов массива = 0'
    else:
        return 0


def check_array(arr):
    for a in arr:
        if int(a) == 0:
            return True
    return False


def get_array():
    arr = []
    while True:
        a = input()
        if a == "":
            return arr
        if a.isdigit():
            arr.append(a)
        else:
            print('число Олег!!!')


def fill_array():
    print("Введите массив, в формате число, затем enter, чтобы закончить ввод элементов, повторите enter")
    return get_array()


print("Ввод первого массива")
arr1 = fill_array()
print("Ввод первого массива завершён, теперь второй")
arr2 = fill_array()
a = catch_exception(arrays_check(arr1, arr2))
if a == 0:
    print(devision_arr(arr1, arr2))
else:
    print(a)

