import numpy as np
import pandas as pd

num_rolls = 1000000
rolls1 = np.random.randint(1, 7, num_rolls)
rolls2 = np.random.randint(1, 7, num_rolls)
sums = rolls1 + rolls2

print(f'Перший кубик: {rolls1}')
print(f'Другий кубик: {rolls2}')
print(f'Сума кубиків: {sums}')
 
sum_counts = pd.value_counts(sums, sort=False)
probabilities = (sum_counts / num_rolls) * 100
prob_table = pd.DataFrame({'Сума': probabilities.index, 'Імовірність (%)': probabilities.values})
print(f'Таблиця імовірностей: \n{prob_table}')
