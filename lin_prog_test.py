import gurobipy as gp
from gurobipy import GRB

# Create empty Model
m = gp.Model('farmer_jones_cakes')

# Add decision variables
c = m.addVar(vtype=GRB.INTEGER, name='c')
v = m.addVar(vtype=GRB.INTEGER, name='v')

# Set objective function
m.setObjective(3 * c + 5 * v, GRB.MAXIMIZE)

# Add constraints
m.addConstr(4 * c + 2 * v <= 32, 'c0')
m.addConstr(4 * c + 5 * v <= 40, 'c1')
m.addConstr(20 * c + 40 * v <= 260, 'c2')

# Solve model
m.optimize()

# Show solution
print('values of attributes')
for v in m.getVars():
    print('%s %g' % (v.varNAme, v.x))


print('Objective value for current solution')
print('Obj: %g' % m.objVal)


# export model
m.write('farmer_jones.lp')
