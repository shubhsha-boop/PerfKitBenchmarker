import collections

samples = [{'metadata': {'key1': 'val1', 'key2': 'val2'}}, {'metadata': {'key1': 'val1', 'key3': 'val3'}}]
unique_values = collections.defaultdict(set)

for sample in samples:
  for k, v in sample['metadata'].items():
    if len(unique_values[k]) < 2 and v.__hash__:
      unique_values[k].add(v)

print(unique_values)
