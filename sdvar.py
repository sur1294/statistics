import math
def mean(data):
  sum = 0
  for num in data:
    sum += num
  return sum / len(data)

def variance(data):
  mean_value = mean(data)
  variance = 0
  for num in data:
    variance += (num - mean_value) ** 2
  variance /= len(data)
  return variance

def standard_deviation(data):
  variance_value = variance(data)
  standard_deviation = math.sqrt(variance_value)
  return standard_deviation

# Test the functions with a sample dataset
data = [1,1,1,8,8,8]
variance_value = variance(data)
standard_deviation_value = standard_deviation(data)
print(variance_value)  
print(standard_deviation_value)  
