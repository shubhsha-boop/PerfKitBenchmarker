import re

with open('perfkitbenchmarker/publisher.py', 'r') as f:
    content = f.read()

content = content.replace(
    'unique_values = {}',
    'unique_values = collections.defaultdict(set)'
)

content = content.replace(
    '        if len(unique_values.setdefault(k, set())) < 2 and v.__hash__:\n          unique_values[k].add(v)',
    '        if len(unique_values[k]) < 2 and v.__hash__:\n          unique_values[k].add(v)'
)

with open('perfkitbenchmarker/publisher.py', 'w') as f:
    f.write(content)
