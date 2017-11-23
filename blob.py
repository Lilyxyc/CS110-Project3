from math import sqrt


class Blob:
    """
    Represents a blob.
    """

    def __init__(self):
        """
        Constructs an empty blob.
        """

        self._P = 0.  # number of pixels
        self._x = 0.  # x-coordinate of center of mass
        self._y = 0.  # y-coordinate of center of mass

    def add(self, i, j):
        """
        Adds pixel (i, j) to this blob.
        """

        oldx = self._P * self._x
        self._x = (oldx + i) / (self._P + 1)

        oldy = self._P * self._y
        self._y = (oldy + j) / (self._P + 1)

        self._P += 1

    def mass(self):
        """
        Returns the number of pixels added to this blob, ie, its mass.
        """

        return self._P

    def distanceTo(self, other):
        """
        Returns the Euclidean distance between the center of mass of this blob
        and the center of mass of other blob.
        """

        dx = self._x - other._x
        dy = self._y - other._y
        return sqrt(dx**2 + dy**2)  # the distance

    def __str__(self):
        """
        Returns a string representation of this blob.
        """

        return '%d (%.4f, %.4f)' % (self._P, self._x, self._y)
