"""
nemplot - Easier plotting with standard formatting

The nemplot package defines simple wrappers for matplotlib's plotting functions
such that all figures have the same format and can be created easily.
"""

import matplotlib
import matplotlib.pyplot as plt

from .plots import *
from .config import *

update_latex_parameters()
