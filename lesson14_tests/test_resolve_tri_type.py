from main import resolve_tri_type
import pytest

def test_resolve_tri_type():
    a, b, c = 3, 4, 5
    result = resolve_tri_type(a, b, c)
    assert result == "Разносторонний"

def test_resolve_tri_type_degree():
    a, b, c = 3, 4, 5
    result = resolve_tri_type(a, b, c)
    assert result == "Прямоугольный"
    a, b, c = 4, 3, 5
    result = resolve_tri_type(a, b, c)
    assert result == "Прямоугольный"
    a, b, c = 3, 5, 4
    result = resolve_tri_type(a, b, c)
    assert result == "Прямоугольный"

def test_resolve_tri_type_same():
    a, b, c = 6, 6, 6
    result = resolve_tri_type(a, b, c)
    assert result == "Равносторонний"

def test_resolve_tri_type_isosceles():
    a, b, c = 6, 5, 6
    result = resolve_tri_type(a, b, c)
    assert result == "Равнобедренный"

    a, b, c = 5, 6, 6
    result = resolve_tri_type(a, b, c)
    assert result == "Равнобедренный"

    a, b, c = 6, 6, 5
    result = resolve_tri_type(a, b, c)
    assert result == "Равнобедренный"

def test_resolve_tri_type_incorrect_input():
    a, b, c = -1, 0, 1
    with pytest.raises(ValueError):
        resolve_tri_type(a, b, c)
