import csv
from pathlib import Path
from typing import Union

from .utils import fahrenheit_to_kelvin


def preprocess_raw_yeast_dataset(
    source_path: Union[Path, str],
    delimiter: str = "\t",
):
    new_rows = list()
    new_rows.append(
        ["temperature_kelvin", "cake_yeast_percentage", "fermentation_hours"]
    )

    with open(source_path) as file:
        iterator = csv.reader(file, delimiter=delimiter)

        try:
            next(iterator)
        except StopIteration:
            return new_rows

        for row in iterator:
            if row is None or len(row) != 5:
                continue

            (
                temperature_fahrenheit,
                _,
                _,
                cake_yeast_percentage,
                fermentation_hours,
            ) = row

            new_rows.append(
                [
                    fahrenheit_to_kelvin(int(temperature_fahrenheit)),
                    float(cake_yeast_percentage),
                    int(fermentation_hours),
                ]
            )

        return new_rows
