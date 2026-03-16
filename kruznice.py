import math

def soucet_polomeru(c1, c2):
    return c1["r"] + c2["r"]

def vzdalenost_stredu(c1, c2):
    x = c1["x"] - c2["x"]
    y = c1["y"] - c2["y"]
    return math.sqrt(x**2 + y**2)

def prunik(c1, c2):
    s = soucet_polomeru(c1, c2)
    d = vzdalenost_stredu(c1, c2)
    if d > s:
        return 0
    if d == s:
        return 1
    if d < s:
        return 2

c1 = {"x": 0, "y": 0, "r": 2}
c2 = {"x": 3, "y": 0, "r": 1}

print(soucet_polomeru(c1, c2))
print(vzdalenost_stredu(c1, c2))
print(prunik(c1, c2))