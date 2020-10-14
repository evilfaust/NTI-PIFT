def get_difference(data_a, data_b):
    ans = 0
    for mark in data_a:
        ans += math.sqrt((data_a[mark]['x'] - data_b[mark]['x']) ** 2 + (data_a[mark]['y'] -
        data_b[mark]['y']) ** 2)
    return ans


print(get_difference(data1, data4))
print(get_difference(data2, data4))
print(get_difference(data3, data4))
