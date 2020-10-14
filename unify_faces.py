def unify_faces(face_data):
    ans = face_data['faceLandmarks']
    for mark in ans:
        ans[mark]['x'] -= face_data['faceRectangle']['left']
        ans[mark]['x'] *= 1000 / face_data['faceRectangle']['width']
        ans[mark]['y'] -= face_data['faceRectangle']['top']
        ans[mark]['y'] *= 1000 / face_data['faceRectangle']['height']
    return ans
    
