import numpy as np
from scipy.stats import f_oneway

# Get data input from the user
data1_str = input("Enter data for group 1 (separated by commas): ")
data2_str = input("Enter data for group 2 (separated by commas): ")
data3_str = input("Enter data for group 3 (separated by commas): ")

# Convert the data strings to lists of numbers
data1 = [float(x) for x in data1_str.split(',')]
data2 = [float(x) for x in data2_str.split(',')]
data3 = [float(x) for x in data3_str.split(',')]

# Perform the ANOVA test
statistic, pvalue = f_oneway(data1, data2, data3)

print(f"ANOVA statistic: {statistic:.3f}")
print(f"p-value: {pvalue:.3f}")
