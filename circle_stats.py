import math

def radius_sum(c1,c2):
    return c1["r"] + c2["r"]

def euclid_distance(c1, c2):
    x = c1["x"] - c2["x"]
    y = c1["y"] - c2["y"]
    return math.sqrt(x ** 2 + y ** 2)

def has_intersection(c1, c2):
    slo = {"is_intersection": 0, "intersections_count": 0}
    s = radius_sum(c1, c2)
    d = euclid_distance(c1, c2)
    if d > s:
        f = 0
    if d == s:
        f = 1
    if d < s:
        f = 2
    is_intersection = False
    if f > 0:
        is_intersection = True
    slo["is_intersection"] = is_intersection
    slo["intersections_count"] = f

    return slo

c1 = {"x": 0, "y": 0, "r": 2}
c2 = {"x": 3, "y": 0, "r": 1}
c3 = {"x": 0, "y": 0, "r": 3}
c4 = {"x": 2, "y": 0, "r": 2}
c5 = {"x": 0, "y": 0, "r": 1}
c6 = {"x": 5, "y": 0, "r": 1}

print(has_intersection(c1, c2))  # dotýkají se
print(has_intersection(c3, c4))  # protínají se
print(has_intersection(c5, c6))  # oddělené