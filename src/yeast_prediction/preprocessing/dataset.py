import csv
from pathlib import Path
from typing import List, Union

from .utils import fahrenheit_to_kelvin


def preprocess_raw_yeast_dataset(
    source_path: Union[Path, str],
    delimiter: str = "\t",
) -> List[List[Union[float, int]]]:
    """
    Preprocesses a dataset in the form of a CSV file.

    Args:
        source_path (Union[Path, str]): A Path or a str representing the file path of
        the dataset you wish to preprocess.
        delimiter (str, optional): The delimiter of the CSV file. Defaults to "\t".

    Returns:
        List[List[Union[float, int]]]: A list of rows that contained the preprocessed
        data.
    """
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
