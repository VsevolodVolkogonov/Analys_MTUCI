from pulp import *

# Initialize the class
model = LpProblem("Волкогонов Всеволод 5 Вариант", LpMaximize)

# Initializing Variables
A = LpVariable('A', lowBound=0, cat='Integer')
B = LpVariable('B', lowBound=0, cat='Integer')

# Determine the profit function
model += 30 * A + 40 * B 

# Add a limit on the total working time
model += 12 * A + 4 * B  <= 300
model += 4 * A + 4 * B <= 120
model += 3 * A + 12 * B <= 252


# Solving
model.solve()

print(f"Необходимо {A.varValue} товаров типа A")
print(f"Необходимо {B.varValue} товаров типа B")
