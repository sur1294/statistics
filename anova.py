import numpy as np
from scipy.stats import f_oneway

# Sample data
data1 = [1, 2, 3, 4, 5]
data2 = [2, 3, 4, 5, 6]
data3 = [3, 4, 5, 6, 7]

# Perform the ANOVA test
statistic, pvalue = f_oneway(data1, data2, data3)

print(f"ANOVA statistic: {statistic:.3f}")
print(f"p-value: {pvalue:.3f}")
