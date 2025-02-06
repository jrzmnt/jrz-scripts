"""
This module defines two classes, R2Vector and R3Vector, which represent 2D and 3D vectors, respectively.

The R2Vector class provides basic vector operations such as addition, subtraction, scalar multiplication,
dot product, and comparison operations. The R3Vector class extends R2Vector to support 3D vectors and
includes an additional method for computing the cross product.

Classes:
    R2Vector: Represents a 2D vector with x and y components.
    R3Vector: Represents a 3D vector with x, y, and z components, inheriting from R2Vector.

Example usage is provided in the main function.
"""

from typing import Union, Type


class R2Vector:
    """Represents a 2D vector with x and y components."""

    def __init__(self, *, x: float, y: float) -> None:
        """
        Initializes a 2D vector.

        Args:
            x (float): The x-component of the vector.
            y (float): The y-component of the vector.
        """
        self.x = x
        self.y = y

    def norm(self) -> float:
        """Returns the Euclidean norm (magnitude) of the vector."""
        return sum(val**2 for val in vars(self).values()) ** 0.5

    def __str__(self) -> str:
        """Returns a string representation of the vector as a tuple."""
        return str(tuple(getattr(self, i) for i in vars(self)))

    def __repr__(self) -> str:
        """Returns a detailed string representation of the vector."""
        arg_list = [f"{key}={val}" for key, val in vars(self).items()]
        args = ", ".join(arg_list)
        return f"{self.__class__.__name__}({args})"

    def __add__(self, other: "R2Vector") -> "R2Vector":
        """Adds two vectors."""
        if type(self) != type(other):
            return NotImplemented
        kwargs = {i: getattr(self, i) + getattr(other, i) for i in vars(self)}
        return self.__class__(**kwargs)

    def __sub__(self, other: "R2Vector") -> "R2Vector":
        """Subtracts one vector from another."""
        if type(self) != type(other):
            return NotImplemented
        kwargs = {i: getattr(self, i) - getattr(other, i) for i in vars(self)}
        return self.__class__(**kwargs)

    def __mul__(self, other: Union[float, "R2Vector"]) -> Union["R2Vector", float]:
        """
        Multiplies the vector by a scalar or computes the dot product with another vector.

        Args:
            other (float or R2Vector): A scalar or another vector.

        Returns:
            R2Vector or float: The result of scalar multiplication or the dot product.
        """
        if isinstance(other, (int, float)):
            kwargs = {i: getattr(self, i) * other for i in vars(self)}
            return self.__class__(**kwargs)
        elif isinstance(other, R2Vector):
            args = [getattr(self, i) * getattr(other, i) for i in vars(self)]
            return sum(args)
        return NotImplemented

    def __eq__(self, other: object) -> bool:
        """Checks if two vectors are equal."""
        if not isinstance(other, R2Vector):
            return NotImplemented
        return all(getattr(self, i) == getattr(other, i) for i in vars(self))

    def __ne__(self, other: object) -> bool:
        """Checks if two vectors are not equal."""
        return not self == other

    def __lt__(self, other: "R2Vector") -> bool:
        """Checks if the norm of this vector is less than the norm of another vector."""
        if type(self) != type(other):
            return NotImplemented
        return self.norm() < other.norm()

    def __gt__(self, other: "R2Vector") -> bool:
        """Checks if the norm of this vector is greater than the norm of another vector."""
        if type(self) != type(other):
            return NotImplemented
        return self.norm() > other.norm()

    def __le__(self, other: "R2Vector") -> bool:
        """Checks if the norm of this vector is less than or equal to the norm of another vector."""
        return not self > other

    def __ge__(self, other: "R2Vector") -> bool:
        """Checks if the norm of this vector is greater than or equal to the norm of another vector."""
        return not self < other


class R3Vector(R2Vector):
    """Represents a 3D vector with x, y, and z components, inheriting from R2Vector."""

    def __init__(self, *, x: float, y: float, z: float) -> None:
        """
        Initializes a 3D vector.

        Args:
            x (float): The x-component of the vector.
            y (float): The y-component of the vector.
            z (float): The z-component of the vector.
        """
        super().__init__(x=x, y=y)
        self.z = z

    def cross(self, other: "R3Vector") -> "R3Vector":
        """
        Computes the cross product of this vector with another 3D vector.

        Args:
            other (R3Vector): Another 3D vector.

        Returns:
            R3Vector: The resulting vector from the cross product.
        """
        if not isinstance(other, R3Vector):
            return NotImplemented
        kwargs = {
            "x": self.y * other.z - self.z * other.y,
            "y": self.z * other.x - self.x * other.z,
            "z": self.x * other.y - self.y * other.x,
        }
        return self.__class__(**kwargs)


def main() -> None:
    """Demonstrates the usage of the R2Vector and R3Vector classes."""
    v1 = R3Vector(x=2, y=3, z=1)
    v2 = R3Vector(x=0.5, y=1.25, z=2)
    print(f"v1 = {v1}")
    print(f"v2 = {v2}")
    v3 = v1 + v2
    print(f"v1 + v2 = {v3}")
    v4 = v1 - v2
    print(f"v1 - v2 = {v4}")
    v5 = v1 * v2
    print(f"v1 * v2 = {v5}")
    v6 = v1.cross(v2)
    print(f"v1 x v2 = {v6}")


if __name__ == "__main__":
    main()
