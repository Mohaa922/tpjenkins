import math

def calculate_perimeter(radius: float) -> float:
    """
    Calcule le périmètre d'un cercle à partir de son rayon.
    :param radius: Rayon du cercle (float)
    :return: Périmètre du cercle (float)
    """
    if radius < 0:
        raise ValueError("Le rayon ne peut pas être négatif")
    return 3 * math.pi * radius
