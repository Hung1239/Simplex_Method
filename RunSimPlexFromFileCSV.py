import numpy as np
import math
import csv
np.seterr(divide='ignore', invalid='ignore')

def hasPositiveValue(vector):
    for element in vector:
        if element > 0:
            return True
    return False
def Maximization():
    matrix_list = []
    list = []
    cf = open("c.csv", "r")
    for c in cf:
        list.append(int(c))
    #print(list)
    #number_of_inequalities = int(input())
    #list.extend(np.zeros(number_of_inequalities).tolist())
    list.extend(np.zeros(3).tolist())
    #print("List:",list)
    """e_values = np.zeros(3)
    e_values[0] = 1"""
    with open('A.csv','rt')as f:
        data = csv.reader(f)
        for row in data:
            matrix_list.append(row)
        #print(values_list)
        # Thêm danh sách
    #matrix_list.append(values_list)
    # Hiện Thị Ma Trận Vừa Nhập
    print(matrix_list)
    coeff_z_array = np.array(list)
    matrix = np.array(matrix_list, dtype=float)
    vr_coeff_array = np.zeros(3, dtype=float)
    zj = np.zeros(9, dtype=float)
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
'''# Test Sucess
matran list
[[2.0, 3.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 8.0], 
 [0.0, 2.0, 5.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 10.0], 
 [3.0, 2.0, 4.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 15.0]]'''