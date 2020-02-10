import pulp

problem = pulp.LpProblem("Paintshop", pulp.LpMaximize)

CiG = pulp.LpVariable("CiG", lowBound=0, cat="Integer")
CiB = pulp.LpVariable("CiB", lowBound=0, cat="Integer")
CiK = pulp.LpVariable("CiK", lowBound=0, cat="Integer")
MiR = pulp.LpVariable("MiR", lowBound=0, cat="Integer")
MiB = pulp.LpVariable("MiB", lowBound=0, cat="Integer")
MiK = pulp.LpVariable("MiK", lowBound=0, cat="Integer")
YiR = pulp.LpVariable("YiR", lowBound=0, cat="Integer")
YiG = pulp.LpVariable("YiG", lowBound=0, cat="Integer")
YiK = pulp.LpVariable("YiK", lowBound=0, cat="Integer")

problem += 10*(MiR + YiR) + 15*(CiG + YiG) + 25*(CiB + MiB) + 25*(CiK + YiK + MiK)
problem += MiR + MiB + MiK <= 5
problem += CiB + CiG + CiK <= 10
problem += YiG + YiR + YiK <= 11
problem += MiR == YiR
problem += CiG == YiG
problem += CiB == MiB
problem += CiK == MiK
problem += CiK == YiK

problem.solve()

print(pulp.value(MiR), pulp.value(MiB), pulp.value(MiK))
print(pulp.value(YiR), pulp.value(YiG), pulp.value(YiK))
print(pulp.value(CiB), pulp.value(CiG), pulp.value(CiK))
print("Red paint: ", pulp.value(MiR + YiR))
print("Green paint: ", pulp.value(CiG + YiG))
print("Blue paint: ", pulp.value(CiB + MiB))
print("Black paint: ", pulp.value(CiK + YiK + MiK))
print("Total profit", pulp.value(problem.objective))
