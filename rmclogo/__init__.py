"""
Topographic Line Art Generator

A Python library for creating Joy Division-style topographic visualizations
from real elevation data.
"""

from .point_map import TopomapGenerator, create_gradient_scaling
from .ridge_map import RidgeMap, FontManager

__version__ = "2.0.0"
__all__ = ["TopomapGenerator", "create_gradient_scaling", "RidgeMap", "FontManager"]
