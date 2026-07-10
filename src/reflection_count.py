"""
Reflection count calculations for various waveguide geometries.
"""

import numpy as np
from typing import Union, List


def planar_reflection_count(
    L: Union[float, np.ndarray], theta: Union[float, np.ndarray], h: float
) -> Union[float, np.ndarray]:
    """
    Calculate reflection count for a planar waveguide.

    Args:
        L: Propagation distance (m)
        theta: Launch angle (radians)
        h: Core half-thickness (m)

    Returns:
        Number of reflections
    """
    return L * np.tan(theta) / (2 * h)


def meridional_reflection_count(
    L: Union[float, np.ndarray], theta: Union[float, np.ndarray], a: float
) -> Union[float, np.ndarray]:
    """
    Calculate reflection count for meridional rays in cylindrical fiber.

    Args:
        L: Propagation distance (m)
        theta: Launch angle (radians)
        a: Core radius (m)

    Returns:
        Number of reflections
    """
    return L * np.tan(theta) / (2 * a)


def skew_reflection_count(
    L: Union[float, np.ndarray],
    theta: Union[float, np.ndarray],
    phi: Union[float, np.ndarray],
    a: float,
) -> Union[float, np.ndarray]:
    """
    Calculate reflection count for skew rays in cylindrical fiber.

    Args:
        L: Propagation distance (m)
        theta: Launch angle (radians)
        phi: Azimuthal angle (radians)
        a: Core radius (m)

    Returns:
        Number of reflections
    """
    return L * np.tan(theta) / (2 * a * np.cos(phi))


def reflection_count_for_angles(
    L: float,
    angles_deg: List[float],
    h: float,
    phi: float = 0.0,
    waveguide_type: str = "planar",
) -> dict:
    """
    Calculate reflection counts for multiple angles.

    Returns:
        Dictionary with angle as key and reflection count as value
    """
    results = {}
    for theta_deg in angles_deg:
        theta = np.radians(theta_deg)
        if waveguide_type == "planar":
            N = planar_reflection_count(L, theta, h)
        else:
            N = skew_reflection_count(L, theta, phi, h)
        results[theta_deg] = N
    return results
