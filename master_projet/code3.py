import numpy as np 
from scipy.integrate import quad 
import matplotlib.pyplot as plt  
import texttable 
 
lamb = np.random.choice(np.arange(1,30), 20, replace=False) 
lamb.sort() 
lamb 
 
def integrand(x, l): 
    return np.exp(l * (np.exp(-x) - 1)) 
 
# Определить функцию moment_Poiss для вычисления интеграла 
def moment_Poiss(l): 
    result, error = quad(integrand, 0, np.inf, args=(l)) 
    return result 
 
inv_poissona = np.array([moment_Poiss(l) for l in lamb]) 
 
 
# Создание таблицы для отображения результатов 
table = texttable.Texttable() 
table.add_rows([['lambda', 'Обратный момент E(1/ X)']] + list(zip(lamb, 
inv_poissona))) 
print(table.draw()) 
 
# Построение графика результатов 
plt.plot(lamb, inv_poissona, 'o-', label='Обратный момент') 
plt.xlabel('lambda') 
plt.ylabel('Обратный Пуассон момент') 
plt.title('Обратный Пуассон момент  при lambda') 
plt.legend() 
plt.show() 
 
 
A_values = np.arange(1, 5) 
 
def integrand(x,A , l): 
    return np.exp(-A * x) * np.exp(l * (np.exp(-x) - 1)) 
 
# Определить функцию moment_Poiss для вычисления интеграла 
def moment_Poiss(A, l): 
    result, error = quad(integrand, 0, np.inf, args=(A , l)) 
60 
 
    return result 
 
moments = np.zeros((len(A_values), len(lamb))) 
 
# Вычислите моменты 
for i, A in enumerate(A_values): 
    for j, l in enumerate(lamb): 
        moments[i, j] = moment_Poiss(A, l) 
         
# Отображение результатов в таблице 
table = texttable.Texttable() 
table.set_max_width(0)
  
rows = [['lambda\\A'] + list(A_values)] 
for j, l in enumerate(lamb): 
    rows.append([l] + list(moments[ :,j])) 
table.add_rows(rows) 

print(table.draw()) 
 
# Построение графика результатов 
fig, ax = plt.subplots(figsize=(8, 6)) 
 
for i, A in enumerate(A_values): 
    ax.plot(lamb, moments[i, :], 'o-', label=f'A = {A}') 
 
ax.set_xlabel('lambda') 
ax.set_ylabel('Обратный  момент') 
ax.set_title('Обратные моменты для различных значений A и lambda') 
ax.legend() 
 
plt.show()