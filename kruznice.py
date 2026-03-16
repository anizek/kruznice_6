# circle_intersection.py

# importujeme funkci z modulu circle_stats
from circle_stats import has_intersection

# definice dvou kružnic
c1 = {"x": 0, "y": 0, "r": 2}
c2 = {"x": 3, "y": 0, "r": 1}

# zjistíme průnik
result = has_intersection(c1, c2)

# výpis výsledku
if result["is_intersection"]:
    print(f"Kružnice se protínají, počet průniků: {result['intersections_count']}")
else:
    print("Kružnice se neprotínají.")

from circles_intersection_draw import draw_data

c1 = {"x": 0, "y": 0, "r": 2}
c2 = {"x": 3, "y": 0, "r": 1}

draw_data(c1, c2)