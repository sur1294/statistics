def median(data):
  data = sorted(data)
  length = len(data)
  if length % 2 == 1:
    return data[length // 2]
  else:
    return mean([data[length // 2 - 1], data[length // 2]])
# Test the function with a sample dataset
data = [1, 2, 3, 4, 5]
median_value = median(data)
print(median_value)  # Output: 3


