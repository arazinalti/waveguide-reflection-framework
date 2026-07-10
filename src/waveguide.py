"""
Waveguide module for optical waveguide analysis.
"""

import numpy as np
from typing import Tuple, Optional


class Waveguide:
    """
    A class representing an optical waveguide for ray optics analysis.

    Attributes:
        core_half_thickness (float): Half-thickness of the core (m)
        core_index (float): Refractive index of the core
        cladding_index (float): Refractive index of the cladding
        alpha_abs (float): Absorption coefficient (m⁻¹)
        alpha_sc (float): Surface scattering coefficient (dimensionless)
    """

    def __init__(
        self,
        core_half_thickness: float = 50e-6,
        core_index: float = 1.45,
        cladding_index: float = 1.44,
        alpha_abs: float = 0.2,
        alpha_sc: float = 5e-5,
    ):
        self.h = core_half_thickness
        self.n1 = core_index
        self.n2 = cladding_index
        self.alpha_abs = alpha_abs
        self.alpha_sc = alpha_sc
        self.theta_c = np.arcsin(self.n2 / self.n1)

    def critical_angle(self) -> float:
        """Return the critical angle for total internal reflection (radians)."""
        return self.theta_c

    def is_total_internal_reflection(self, theta: float) -> bool:
        """Check if the ray angle satisfies TIR condition."""
        return theta > self.theta_c

    def reflection_count(self, L: float, theta: float, phi: float = 0.0) -> float:
        """
        Calculate the number of internal reflections.

        Args:
            L: Propagation distance (m)
            theta: Launch angle relative to axis (radians)
            phi: Azimuthal angle for skew rays (radians), default 0 for meridional

        Returns:
            Number of reflections
        """
        if phi == 0:
            return L * np.tan(theta) / (2 * self.h)
        else:
            return L * np.tan(theta) / (2 * self.h * np.cos(phi))

    def real_path_length(self, L: float, theta: float) -> float:
        """Calculate the actual path length traveled by the ray."""
        return L / np.cos(theta)

    def attenuation_coefficient(self, theta: float, phi: float = 0.0) -> float:
        """
        Calculate the equivalent attenuation coefficient.

        Returns:
            Equivalent attenuation coefficient (m⁻¹)
        """
        return self.alpha_abs / np.cos(theta) + self.alpha_sc * np.tan(theta) / (
            2 * self.h * np.cos(phi) if phi != 0 else 1
        )

    def transmitted_power(
        self, L: float, theta: float, phi: float = 0.0, P0: float = 1.0
    ) -> float:
        """
        Calculate the transmitted power using the two-parameter model.

        Returns:
            Normalized transmitted power P/P₀
        """
        N = self.reflection_count(L, theta, phi)
        L_real = self.real_path_length(L, theta)
        return P0 * np.exp(-self.alpha_abs * L_real - self.alpha_sc * N)

    def optimal_launch_angle(self) -> float:
        """
        Calculate the optimal launch angle that minimizes loss.

        Returns:
            Optimal angle (radians)
        """
        if self.alpha_sc / (2 * self.h * self.alpha_abs) <= 1:
            return np.arcsin(self.alpha_sc / (2 * self.h * self.alpha_abs))
        else:
            return 0.0
