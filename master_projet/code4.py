import numpy as np 
from scipy.integrate import quad 
import matplotlib.pyplot as plt  
import texttable 
 
alph_values = np.random.choice(np.arange(2, 20), 15, replace=False) 
alph_values.sort() 
bet_values = [2, 3, 4] 
 
 
def integrate(x, a, b): 
    return  ((1 + x / b) ** (-a)) 
 
def inverse_moment( a, b): 
    result, error = quad(integrate, 0, np.inf, args=( a, b)) 
    return result 
 
# Вычисление первого момента для каждой пары (альфа, бета) 
first_moment = [[inverse_moment(a, b) for b in bet_values] for a in alph_values] 
 
table = texttable.Texttable() 
table.set_max_width(0) 
rows = [['alpha \\ beta'] + bet_values] 
 
# Заполнение строк Альфа-значениями и вычисленными моментами 
rows = [['alpha \\ beta'] + [str(b) for b in bet_values]] 
 
for i, a in enumerate(alph_values): 
    row = [a] + [first_moment[i][j] for j in range(len(bet_values))] 
    rows.append(row) 
table.add_rows(rows) 
print(table.draw()) 
 
# Построить график для каждой Альфы 
first_moment_array = np.array(first_moment)  # Преобразовать список в массив 
numpy для индексации 
for j, b in enumerate(bet_values): 
    plt.plot(alph_values, first_moment_array[:, j], marker='o', linestyle='-', 
label=f'beta = {b}') 
 
plt.xlabel('Альфа-значения') 
plt.ylabel('обратный момент E(1/X)') 
plt.title(f'обратный момент E(1/X) по альфа при различных бета') 
plt.legend() 
62 
 
plt.grid(True) 
plt.show() 
 
 
A_values = 1 
 
def integrate(x, A, a, b): 
    return np.exp(-A * x) * ((1 + x / b) ** (-a)) 
 
def inverse_moment(A, a, b): 
    result, error = quad(integrate, 0, np.inf, args=(A, a, b)) 
    return result 
 
# Вычисление первого момента для каждой пары (альфа, бета) 
first_moments = [[inverse_moment(A_values, a, b) for b in bet_values] for a in 
alph_values] 
 
plt.figure(figsize=(8,6)) 
table = texttable.Texttable() 
table.set_max_width(0) 
rows = [['alpha \\ beta'] + bet_values] 
 
# Заполнение строк Альфа-значениями и вычисленными моментами 
rows = [['alpha \\ beta'] + [str(b) for b in bet_values]] 
 
for i, a in enumerate(alph_values): 
    row = [a] + [first_moments[i][j] for j in range(len(bet_values))] 
    rows.append(row) 
table.add_rows(rows) 
print(table.draw()) 
 
# Построить график для каждой Альфы 
first_moment_array = np.array(first_moment)  # Преобразовать список в массив 
numpy для индексации 
for j, b in enumerate(bet_values): 
    plt.plot(alph_values, first_moment_array[:, j], marker='o', linestyle='-', 
label=f'beta = {b}') 
 
plt.xlabel('Альфа-значения') 
plt.ylabel('обратный момент E(1/X + 1)') 
plt.title(f'обратный момент E(1/X + A) по альфа при различных бета и A = 1') 
plt.legend() 
plt.grid(True) 
plt.show()