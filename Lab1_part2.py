import numpy as np



def min_of_Func(d):
    return min(d[0])



def enable_column_index(d):
    return list(d[0]).index(min_of_Func(d))



def enable_string(d, len_of_strings):
    ratio = []  
    for i in range(len_of_strings):
        ratio.append(d[i][-1] / d[i][enable_column_index(d)])
    m = max(ratio)
    m_index = ratio.index(m)  
    for i in range(len_of_strings):  
        ri = ratio[i]
        if 0 < ri < m:
            m = ri
            m_index = i
    return m_index



def enable_element(d, len_of_strings):
    return d[enable_string(d, len_of_strings)][enable_column_index(d)]


def column_processing(len_of_strings, len_of_columns):
    global d
    en_str = enable_string(d, len_of_strings)  
    en_col = enable_column_index(d)  
    en_el = d[en_str][en_col]  
    result_d = []  
    for i in range(len_of_strings):
        if i != en_str:
            processing_line = list(d[i])  
            k = d[i][en_col] / en_el  
            for j in range(len_of_columns):  
                processing_line[j] = processing_line[j] - k * d[en_str][j]
            result_d.append(processing_line)
        else:  
            result_d.append(list(d[en_str]))
    d = result_d  


def solve(len_of_strings, len_of_columns):
    global d
    while True:
        if min(list(d[0])) >= 0:  
            break
        else:
            column_processing(len_of_strings, len_of_columns)



def determinate_of_basis(len_of_strings, len_of_columns):
    basis = ""
    len_of_basis = len_of_columns - len_of_strings
    for i in range(len_of_basis):
        basis += "x" + str(i + 1) + " "
    return len_of_basis, basis



def found_odds_of_nonzero_element(d, basis, len_of_strings):
    odds = [0] * basis
    for i in range(len_of_strings):
        for j in range(basis):
            if d[i][j] != 0:
                odds[j] = d[i][j]
    return odds


def printSolution(d, len_of_strings, len_of_columns):
    for i in range(len_of_strings):
        print(d[i])
    bas = determinate_of_basis(len_of_strings, len_of_columns)
    basis = bas[0]
    odds = found_odds_of_nonzero_element(d, basis, len_of_strings)
    print("Базисными переменными являются:", bas[1])
    print("Максимальное значение функции:", d[0][-1])
    print("Максимум функции достигается при значениях:", end="")
    for i in range(basis):
        print("x" + str(i + 1) + " = " + str(d[i + 1][-1] / odds[i]) + "; ", end="")


d = np.loadtxt("/alexg/Sial/coef.txt", dtype=np.float64)
len_of_strings, len_of_columns = d.shape
solve(len_of_strings, len_of_columns)
printSolution(d, len_of_strings, len_of_columns)

