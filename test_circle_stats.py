import pytest
from circle_stats import has_intersection, radius_sum

def test_has_intersection_cases():
    # běžné
    c1 = {"x":0,"y":0,"r":2}
    c2 = {"x":3,"y":0,"r":1}
    assert has_intersection(c1,c2) == {"is_intersection": True, "intersections_count": 1}

    c3 = {"x":0,"y":0,"r":3}
    c4 = {"x":2,"y":0,"r":2}
    assert has_intersection(c3,c4) == {"is_intersection": True, "intersections_count": 2}

    # hraniční
    c5 = {"x":0,"y":0,"r":2}
    c6 = {"x":5,"y":0,"r":3}
    # ❌ špatný expected output pro trénink čtení failu
    assert has_intersection(c5,c6) == {"is_intersection": True, "intersections_count": 2}

    c7 = {"x":0,"y":0,"r":2}
    c8 = {"x":0,"y":4,"r":2}
    assert has_intersection(c7,c8) == {"is_intersection": True, "intersections_count": 1}

    # negativní
    c9 = {"x":0,"y":0,"r":1}
    c10 = {"x":5,"y":5,"r":1}
    assert has_intersection(c9,c10) == {"is_intersection": False, "intersections_count": 0}

def test_radius_sum_case():
    c1 = {"x":0,"y":0,"r":2}
    c2 = {"x":3,"y":0,"r":1}
    assert radius_sum(c1,c2) == 3