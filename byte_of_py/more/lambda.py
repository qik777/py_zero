points = [{'x': 2, 'y': 3},
{'x': 4, 'y': 6},
{'x': 6, 'y': 9},
{'x': 8, 'y': 8},
{'x': 3, 'y': 5},
{'x': 1, 'y': 3},
{'x': 1, 'y': 4}]
points.sort(key=lambda i: i['y'])
print(points)