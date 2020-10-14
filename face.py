import json

def get_json(filename):
    with open(filename, 'r') as f:
        json_string = f.read()
        data = json.loads(json_string)
        f.close()
        return data
    return None

data1 = get_json('1.json')
data2 = get_json('2.json')
data3 = get_json('3.json')
data4 = get_json('who_is.json')

print(data1)
print(data2)
print(data3)
print(data4)
