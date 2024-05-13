import pytest
from perimeter import calculate_perimeter, calculate_area

def test_perimeter():
    assert calculate_perimeter(6) == 24

def test_area():
    assert calculate_area(6) == 36

