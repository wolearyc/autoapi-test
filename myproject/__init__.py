"""Main file."""

import numpy as np
from numpy.typing import NDArray
from typing import Sequence


def my_function(x: NDArray[np.float64]):
    """Do something.

    Parameters
    ----------
    x
        type hint doesn't link!
    """
    pass


class MyClass(Sequence[NDArray[np.float64]]):
    """My class.

    The base class works for some reason.
    """

    def __init__(self):
        pass

    def my_method(self, x: NDArray[np.float64]):
        """Do something.

        Parameters
        ----------
        x
            type hint doesn't link!
        """
        pass

    def another_method(self, x: Sequence[NDArray[np.float64]]):
        """Do something.

        Parameters
        ----------
        x
            type hint doesn't link!
        """
        pass
