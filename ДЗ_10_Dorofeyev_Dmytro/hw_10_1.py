import pulp

# Define the linear programming problem (maximize total production)
model = pulp.LpProblem("Production_Optimization", pulp.LpMaximize)

# Define decision variables (number of Lemonade and Fruit Juice to produce)
lemonade = pulp.LpVariable("Lemonade", lowBound=0, cat='Integer')
fruit_juice = pulp.LpVariable("Fruit_Juice", lowBound=0, cat='Integer')

# Define the objective function (maximize total production)
model += lemonade + fruit_juice, "Total_Production"

# Define resource constraints
model += 2 * lemonade + 1 * fruit_juice <= 100, "Water_Constraint"  # Water limit
model += 1 * lemonade <= 50, "Sugar_Constraint"  # Sugar limit
model += 1 * lemonade <= 30, "Lemon_Juice_Constraint"  # Lemon juice limit
model += 2 * fruit_juice <= 40, "Fruit_Puree_Constraint"  # Fruit puree limit

# Solve the optimization problem
model.solve()

# Output results
print("Optimal Production Plan:")
print(f"Lemonade: {pulp.value(lemonade)} units")
print(f"Fruit Juice: {pulp.value(fruit_juice)} units")
print(f"Total Production: {pulp.value(model.objective)} units")
