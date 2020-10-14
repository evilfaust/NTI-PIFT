import json
import math


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


def unify_faces(face_data):
    ans = face_data['faceLandmarks']
    for mark in ans:
        ans[mark]['x'] -= face_data['faceRectangle']['left']
        ans[mark]['x'] *= 1000 / face_data['faceRectangle']['width']
        ans[mark]['y'] -= face_data['faceRectangle']['top']
        ans[mark]['y'] *= 1000 / face_data['faceRectangle']['height']
    return ans


data1 = unify_faces(data1)
data2 = unify_faces(data2)
data3 = unify_faces(data3)
data4 = unify_faces(data4)

print(data1)
print(data2)
print(data3)
print(data4)

def get_difference(data_a, data_b):
    ans = 0
    for mark in data_a:
        ans += math.sqrt((data_a[mark]['x'] - data_b[mark]['x']) ** 2 + (data_a[mark]['y'] -
        data_b[mark]['y']) ** 2)
    return ans


print(get_difference(data1, data4))
print(get_difference(data2, data4))
print(get_difference(data3, data4))
print('=======================================')
print(get_difference(data1, data3))
