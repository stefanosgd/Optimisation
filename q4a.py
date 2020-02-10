import pulp

problem = pulp.LpProblem("Luggage", pulp.LpMaximize)

A = pulp.LpVariable("ItemA", lowBound=0, upBound=1, cat="Integer")
B = pulp.LpVariable("ItemB", lowBound=0, upBound=1, cat="Integer")
C = pulp.LpVariable("ItemC", lowBound=0, upBound=1, cat="Integer")
D = pulp.LpVariable("ItemD", lowBound=0, upBound=1, cat="Integer")
E = pulp.LpVariable("ItemE", lowBound=0, upBound=1, cat="Integer")
F = pulp.LpVariable("ItemF", lowBound=0, upBound=1, cat="Integer")


problem += 60*A + 70*B + 40*C + 70*D + 16*E + 100*F
problem += 6*A + 7*B + 4*C + 9*D + 3*E + 8*F <= 20

problem.solve()

print("Item A taken?", bool(pulp.value(A)))
print("Item B taken?", bool(pulp.value(B)))
print("Item C taken?", bool(pulp.value(C)))
print("Item D taken?", bool(pulp.value(D)))
print("Item E taken?", bool(pulp.value(E)))
print("Item F taken?", bool(pulp.value(F)))
print("Total value:", pulp.value(problem.objective))
