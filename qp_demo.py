#!/usr/bin/python3

import pandas as pd
from pandas import DataFrame
from docplex.mp.advmodel import AdvModel as Model


# Matrix of objective function coefficients

c = [700 / 1, 700 / 2, 700 / 3, 700 / 4, 700 / 5]
e = [500 / 1, 500 / 2, 500 / 3, 500 / 4, 500 / 5]


var = {
        'consolidate': [round(num, 1) for num in c],
        'express': [round(num, 1) for num in e]
}

units = list(range(1,6))

dfv = pd.DataFrame(var, index=units)


# Create the model
m = Model(name='quadratic_transportation')

# Create variables
dep_var = m.integer_var_list(dfv.columns, name='department', lb=2)

# Add constraints


deps = ['consolidate', 'express']

# Create objective function
total_cost = m.sum(var[dep][u - 1] * u for dep in deps for u in units)

m.minimize(total_cost)

m.solve()

m.print_solution()

m.print_information()
