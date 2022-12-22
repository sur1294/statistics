def mode(data):
  counts = {}
  for num in data:
    if num in counts:
      counts[num] += 1
    else:
      counts[num] = 1

  max_count = max(counts.values())
  modes = []
  for num, count in counts.items():
    if count == max_count:
      modes.append(num)

  return modes

# Test the function with a sample dataset
data = [1, 2, 3, 3, 4, 5]
mode_value = mode(data)
print(mode_value)  # Output: [3]


