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
