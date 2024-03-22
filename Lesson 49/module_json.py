import json

test_data = {10: 100,
             20: 800,
             30: ['a', 'b', 'c'],}

json.dump(test_data, open('test.json', 'w'))

json_var = json.load(open('test.json', 'r'))
print(json_var)
