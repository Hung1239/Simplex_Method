import numpy as np
import math
np.seterr(divide='ignore', invalid='ignore')

def hasPositiveValue(vector):
    for element in vector:
        if element > 0:
            return True
    return False
def Maximization():
    matrix_list = []
    print('Nhap so bien của Z:')
    number_of_variables = int(input())
    list = []
    for i in range(number_of_variables):
        print("Biến x", i + 1, ": ")
        val = int(input())
        list.append(val)
    print('Số Hàng điều kiện: ')
    number_of_inequalities = int(input())
    list.extend(np.zeros(number_of_inequalities).tolist())
    print("List:",list)
    e_values = np.zeros(number_of_inequalities)
    e_values[0] = 1
    for i in range(number_of_inequalities):
        values_list = []
        f = open("test.txt", "r")
        for value in f:
            print("Biến x ", value, "của hàng thứ", value)
            value = float(input())
            values_list.append(value)
        values_list = []
        f = open("test.txt", "r")
        for j in range(number_of_variables):
            print("Biến x ",j+1,"của hàng thứ",i + 1)
            value = float(input())
            values_list.append(value)
        if i != 0:
            e_values[i - 1] = 0
            e_values[i] = 1
        for e_value in e_values:
            values_list.append(e_value)
        print('Nhập vế kết quả của hàng thứ', i + 1)
        res = float(input())
        # construct our list
        values_list.append(res)
        # Thêm danh sách
        matrix_list.append(values_list)
    # Hiện Thị Ma Trận Vừa Nhập
    print(matrix_list)

    coeff_z_array = np.array(list)
    matrix = np.array(matrix_list, dtype=float)
    vr_coeff_array = np.zeros(number_of_inequalities, dtype=float)
    zj = np.zeros(number_of_variables + number_of_inequalities, dtype=float)
    cj_minus_zj = coeff_z_array - zj

    # first iteration
    while hasPositiveValue(cj_minus_zj):
        # find the index of the max element in the array
        max_index = int(np.where(cj_minus_zj == max(cj_minus_zj))[0])
        print('MAX INDEX : ', max_index)
        # extract the pivot fector and flatten it
        pivot_vector = matrix[:, max_index:max_index + 1]
        pivot_vector = pivot_vector.flatten()
        # extract bj values
        bj = matrix[:, -1]
        # extract sorted values by dividing bj by pivot vector
        vs = np.divide(bj, pivot_vector)
        vs[vs < 0] = math.nan
        # extract the index of the min element in the array so we know the pivot element
        min_index = int(np.where(vs == min(vs))[0])
        matrix[min_index] = matrix[min_index] / matrix[min_index, max_index]
        vr_coeff_array[min_index] = coeff_z_array[max_index]
        for index in range(len(matrix)):
            if index != min_index:
                coeff = matrix[index, max_index]
                if coeff != 0:
                    matrix[index] = matrix[index] - matrix[min_index] * coeff
        # loop through each variable
        for index in range(len(matrix[0, :-1])):
            # scalar product
            n = np.dot(matrix[:, index], vr_coeff_array)
            zj[index] = n
        cj_minus_zj = coeff_z_array - zj

        print("Giá trị Max = ", np.dot(vr_coeff_array, bj))


print("Simple Method")
Maximization()
