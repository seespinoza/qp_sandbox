#!/usr/bin/python

from docplex.mp.model import Model

def calc_slope(fee, units):
    slopes = [(0, 0)]
    for u in range(1, units + 1):

        # Cost for transporting one unit
        u_cost = round(fee / u, 2)
        slopes.append(tuple((u, u_cost)))

    return slopes

# Fees
UNITS = 3

e_fee = 100
con_fee = 50
org_fee = 200

# build model
pm = Model(name='piecewise_test')


# Create Decision Variables
e = pm.integer_var(name='e')
c = pm.integer_var(name='c')
o = pm.integer_var(name='o')

ey = pm.continuous_var(name='ey')
cy = pm.continuous_var(name='cy')
oy = pm.continuous_var(name='oy')

# Calculate Break points for PFs
breaks1 = calc_slope(e_fee, UNITS)
breaks2 = calc_slope(con_fee, UNITS)
breaks3 = calc_slope(org_fee, UNITS)

# Piecewise Functions
pwe = pm.piecewise(preslope=0, breaksxy=breaks1, postslope=1)
pwc = pm.piecewise(preslope=0, breaksxy=breaks2, postslope=1)
pwo = pm.piecewise(preslope=0, breaksxy=breaks3, postslope=1)

# Create Piecewise Constraints
pm.add_constraint(ey == pwe(e))
pm.add_constraint(cy == pwc(c))
pm.add_constraint(oy == pwo(o))

# Other constraints
pm.add_constraint(e + c + o == 5)
pm.add_constraint(e <= 3)
pm.add_constraint(c <= 3)
pm.add_constraint(o <= 3)


# Objective Function
pm.minimize(ey + cy + oy)
pm.print_information()

s = pm.solve()
pm.print_solution()
pm.export_as_lp('piecewise_test')
