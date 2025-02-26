import pytest
from calculator import calculate_perimeter

def test_calculate_perimeter():
    # Test avec un rayon valide
    assert round(calculate_perimeter(5), 2) == 31.42  # 2 * π * 5 ≈ 31.42

    # Test avec un rayon nul
    assert calculate_perimeter(0) == 0

    # Test avec un rayon négatif (doit lever une exception)
    with pytest.raises(ValueError, match="Le rayon ne peut pas être négatif"):
        calculate_perimeter(-5)
