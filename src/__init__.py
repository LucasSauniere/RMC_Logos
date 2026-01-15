"""
Topographic Line Art Generator

A Python library for creating Joy Division-style topographic visualizations
from real elevation data.
"""

from .topomap import TopomapGenerator, create_gradient_scaling

__version__ = "2.0.0"
__all__ = ["TopomapGenerator", "create_gradient_scaling"]
