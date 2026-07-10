"""
Two-parameter attenuation model for optical waveguides.
"""

import numpy as np
from typing import Tuple, Optional


class AttenuationModel:
    """
    Two-parameter attenuation model separating absorption and surface scattering.
    """

    def __init__(
        self, alpha_abs: float = 0.2, alpha_sc: float = 5e-5, h: float = 50e-6
    ):
        self.alpha_abs = alpha_abs
        self.alpha_sc = alpha_sc
        self.h = h

    def absorption_loss(self, L: float, theta: float) -> float:
        """Calculate absorption loss component."""
        return self.alpha_abs * L / np.cos(theta)

    def scattering_loss(self, L: float, theta: float) -> float:
        """Calculate surface scattering loss component."""
        return self.alpha_sc * L * np.tan(theta) / (2 * self.h)

    def total_loss(self, L: float, theta: float) -> float:
        """Calculate total loss."""
        return self.absorption_loss(L, theta) + self.scattering_loss(L, theta)

    def transmitted_power(self, L: float, theta: float, P0: float = 1.0) -> float:
        """Calculate transmitted power."""
        return P0 * np.exp(-self.total_loss(L, theta))

    def classical_power(self, L: float, P0: float = 1.0) -> float:
        """Calculate classical exponential attenuation."""
        return P0 * np.exp(-self.alpha_abs * L)

    def equivalent_alpha(self, theta: float) -> float:
        """Calculate equivalent attenuation coefficient."""
        return self.alpha_abs / np.cos(theta) + self.alpha_sc * np.tan(theta) / (
            2 * self.h
        )
