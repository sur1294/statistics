def data_range(data):
  min_value = min(data)
  max_value = max(data)
  data_range = max_value - min_value
  return data_range

# Test the function with a sample dataset
data = [1, 2, 3, 4, 5]
range_value = data_range(data)
print(range_value)  # Output: 4
