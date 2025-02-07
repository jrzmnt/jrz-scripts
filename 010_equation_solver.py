from abc import ABC, abstractmethod
import re
from typing import Dict, List, Union


class Equation(ABC):
    """
    Abstract base class representing a mathematical equation.

    Attributes:
        degree (int): The degree of the equation.
        type (str): The type of the equation.
        coefficients (Dict[int, Union[int, float]]): A dictionary mapping powers of x to their coefficients.
    """

    degree: int
    type: str

    def __init__(self, *args: Union[int, float]) -> None:
        """
        Initializes an Equation object.

        Args:
            *args: Coefficients of the equation, starting from the highest degree.

        Raises:
            TypeError: If the number of arguments does not match the degree + 1 or if any coefficient is not an int or float.
            ValueError: If the highest degree coefficient is zero.
        """
        if (self.degree + 1) != len(args):
            raise TypeError(
                f"'Equation' object takes {self.degree + 1} positional arguments but {len(args)} were given"
            )
        if any(not isinstance(arg, (int, float)) for arg in args):
            raise TypeError("Coefficients must be of type 'int' or 'float'")
        if args[0] == 0:
            raise ValueError("Highest degree coefficient must be different from zero")
        self.coefficients = {(len(args) - n - 1): arg for n, arg in enumerate(args)}

    def __init_subclass__(cls) -> None:
        """
        Validates that subclasses have the required attributes 'degree' and 'type'.

        Raises:
            AttributeError: If 'degree' or 'type' attributes are missing in the subclass.
        """
        if not hasattr(cls, "degree"):
            raise AttributeError(
                f"Cannot create '{cls.__name__}' class: missing required attribute 'degree'"
            )
        if not hasattr(cls, "type"):
            raise AttributeError(
                f"Cannot create '{cls.__name__}' class: missing required attribute 'type'"
            )

    def __str__(self) -> str:
        """
        Returns a string representation of the equation.

        Returns:
            str: The equation in a readable format.
        """
        terms = []
        for n, coefficient in self.coefficients.items():
            if not coefficient:
                continue
            if n == 0:
                terms.append(f"{coefficient:+}")
            elif n == 1:
                terms.append(f"{coefficient:+}x")
            else:
                terms.append(f"{coefficient:+}x**{n}")
        equation_string = " ".join(terms) + " = 0"
        return re.sub(r"(?<!\d)1(?=x)", "", equation_string.strip("+"))

    @abstractmethod
    def solve(self) -> List[float]:
        """
        Solves the equation.

        Returns:
            List[float]: A list of solutions to the equation.
        """
        pass

    @abstractmethod
    def analyze(self) -> Dict[str, Union[float, str]]:
        """
        Analyzes the equation and returns key properties.

        Returns:
            Dict[str, Union[float, str]]: A dictionary containing analysis results.
        """
        pass


class LinearEquation(Equation):
    degree = 1
    type = "Linear Equation"

    def solve(self) -> List[float]:
        """
        Solves the linear equation.

        Returns:
            List[float]: A list containing the solution to the equation.
        """
        a, b = self.coefficients.values()
        x = -b / a
        return [x]

    def analyze(self) -> Dict[str, float]:
        """
        Analyzes the linear equation.

        Returns:
            Dict[str, float]: A dictionary containing the slope and y-intercept of the line.
        """
        slope, intercept = self.coefficients.values()
        return {"slope": slope, "intercept": intercept}


class QuadraticEquation(Equation):
    degree = 2
    type = "Quadratic Equation"

    def __init__(self, *args: Union[int, float]) -> None:
        """
        Initializes a QuadraticEquation object.

        Args:
            *args: Coefficients of the quadratic equation, starting from the highest degree.
        """
        super().__init__(*args)
        a, b, c = self.coefficients.values()
        self.delta = b**2 - 4 * a * c

    def solve(self) -> List[float]:
        """
        Solves the quadratic equation.

        Returns:
            List[float]: A list of real roots of the equation.
        """
        if self.delta < 0:
            return []
        a, b, _ = self.coefficients.values()
        x1 = (-b + (self.delta) ** 0.5) / (2 * a)
        x2 = (-b - (self.delta) ** 0.5) / (2 * a)
        if self.delta == 0:
            return [x1]
        return [x1, x2]

    def analyze(self) -> Dict[str, Union[float, str]]:
        """
        Analyzes the quadratic equation.

        Returns:
            Dict[str, Union[float, str]]: A dictionary containing the vertex, concavity, and min/max information.
        """
        a, b, c = self.coefficients.values()
        x = -b / (2 * a)
        y = a * x**2 + b * x + c
        if a > 0:
            concavity = "upwards"
            min_max = "min"
        else:
            concavity = "downwards"
            min_max = "max"
        return {"x": x, "y": y, "min_max": min_max, "concavity": concavity}


def solver(equation: Equation) -> str:
    """
    Solves and analyzes an equation, returning a formatted string with the results.

    Args:
        equation (Equation): An instance of a subclass of Equation.

    Returns:
        str: A formatted string containing the equation, solutions, and analysis details.

    Raises:
        TypeError: If the argument is not an instance of Equation.
    """
    if not isinstance(equation, Equation):
        raise TypeError("Argument must be an Equation object")

    output_string = f"\n{equation.type:-^24}"
    output_string += f"\n\n{equation!s:^24}\n\n"
    output_string += f'{"Solutions":-^24}\n\n'
    results = equation.solve()
    match results:
        case []:
            result_list = ["No real roots"]
        case [x]:
            result_list = [f"x = {x:+.3f}"]
        case [x1, x2]:
            result_list = [f"x1 = {x1:+.3f}", f"x2 = {x2:+.3f}"]
    for result in result_list:
        output_string += f"{result:^24}\n"
    output_string += f'\n{"Details":-^24}\n\n'
    details = equation.analyze()
    match details:
        case {"slope": slope, "intercept": intercept}:
            details_list = [
                f"slope = {slope:>16.3f}",
                f"y-intercept = {intercept:>10.3f}",
            ]
        case {"x": x, "y": y, "min_max": min_max, "concavity": concavity}:
            coord = f"({x:.3f}, {y:.3f})"
            details_list = [f"concavity = {concavity:>12}", f"{min_max} = {coord:>18}"]
    for detail in details_list:
        output_string += f"{detail}\n"
    return output_string


def main() -> None:
    """
    Main function to demonstrate the functionality of the Equation classes and solver.
    """
    lin_eq = LinearEquation(2, 3)
    quadr_eq = QuadraticEquation(1, 2, 1)
    print(solver(quadr_eq))
    print(solver(lin_eq))


if __name__ == "__main__":
    main()
