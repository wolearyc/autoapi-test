"""Main file."""

import numpy as np
from numpy.typing import NDArray
from typing import Sequence, Any


def function_a(x: NDArray[np.float64]):
    """Do something.

    Parameters
    ----------
    x
        type hint doesn't link
    """
    pass


def function_b(x: NDArray):
    """Do something.

    Parameters
    ----------
    x
        type hint doesn't link
    """
    pass


def function_b(x: np.ndarray):
    """Do something.

    Parameters
    ----------
    x
        type hint works as expected
    """
    pass


def function_b(x: np.ndarray[Any, np.dtype[np.float64]]):
    """Do something.

    Parameters
    ----------
    x
        type hint works as expected
    """
    pass
