import numpy as np 
import scipy 
import matplotlib.pyplot as plt  
import texttable 
 
lamda = np.linspace(0, 1, 10)[:-1] 
A_values = np.arange(1, 4) 
 
def funct_hypergeo(A_values, lamda): 
    moment = [] 
    for A in A_values: 
        a = A + 1 
        b = 2 
        c = A + 2 
        moment_for_A = [scipy.special.hyp2f1(a, b, c, l) for l in lamda] 
        moment.append(moment_for_A) 
    return moment 
def inverse_hypergeo(lamda, A_values, func_geo): 
    inverse_results = [] 
    for A, moment_for_A in zip(A_values, func_geo): 
        inverse_result_for_A = [(((1 - l) ** 2) / (A + 1)) * moment for l, moment 
in zip(lamda, moment_for_A)] 
        inverse_results.append(inverse_result_for_A) 
    return inverse_results 
 
# Вычислить обратную функцию для каждого значения 
first_inverse_moment = inverse_hypergeo(lamda, A_values, func_geo) 
 
 
tableau = [[ " A ","  Параметр Ламбды ", "Обратный момент E(1 / X + A)"]] 
     
plt.figure() 
for interger, ivs in zip(A_values, first_inverse_moment): 
    tableau.append(["A = {0}".format(interger), "", ""]) 
    for l, iv in zip(lamda, ivs): 
        tableau.append(["", l, iv]) 
    plt.plot(lamda, ivs, 'o-', label=f'A={interger}') 
 
plt.legend() 
plt.xlabel('lambda') 
plt.ylabel('Обратный гипергеометрический момент\n E(1/X + A)') 
plt.title('Обратные гипергеометрические моменты для различных A') 
plt.show() 
 
56 
 
# Распечатайте таблицу результатов 
results_table = texttable.Texttable() 
results_table.add_rows(tableau) 
print(results_table.draw())