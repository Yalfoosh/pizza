from typing import Union


def fahrenheit_to_kelvin(temperature_in_fahrenheit: Union[float, int]) -> float:
    """
    Converts a value from the Fahrenheit scale to the equivalent value on the Kelvin
    scale.

    Args:
        temperature_in_fahrenheit (Union[float, int]): A float or int representing the
        value of a temperature on the Fahrenheit scale you wish to convert to the
        Kelvin scale.

    Returns:
        float: Argument temperature_in_fahrenheit converted to the Kelvin scale.
    """
    return (temperature_in_fahrenheit + 459.67) * 5 / 9
