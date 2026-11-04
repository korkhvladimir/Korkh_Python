import sys
from decimal import Decimal, ROUND_HALF_UP
from typing import Dict, Tuple


def round_half_up(value: float) -> float:
    """Округление до десятых по правилу 'половина вверх'."""
    return float(
        Decimal(str(value)).quantize(
            Decimal("0.1"),
            rounding=ROUND_HALF_UP
        )
    )


def process_measurements(
    file_path: str
) -> Dict[str, Tuple[float, float, float, int]]:
    """
    Читает файл построчно и агрегирует данные по станциям.

    Возвращает словарь:
    {
        станция: (min_temp, max_temp, sum_temp, count)
    }
    """

    stations: Dict[str, Tuple[float, float, float, int]] = {}

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.rstrip("\n")

                if not line:
                    continue

                station, temp_str = line.split(";", 1)
                temp = float(temp_str)

                if station not in stations:
                    stations[station] = (
                        temp,
                        temp,
                        temp,
                        1
                    )
                else:
                    min_t, max_t, sum_t, count = stations[station]

                    stations[station] = (
                        temp if temp < min_t else min_t,
                        temp if temp > max_t else max_t,
                        sum_t + temp,
                        count + 1
                    )

    except FileNotFoundError:
        sys.stderr.write(
            f"Ошибка: файл '{file_path}' не найден.\n"
        )
        sys.exit(1)

    return stations


def print_results(
    stations: Dict[str, Tuple[float, float, float, int]]
) -> None:
    """
    Выводит результаты в формате:
    <станция>;<min>;<mean>;<max>
    """

    for station in sorted(stations):
        min_t, max_t, sum_t, count = stations[station]

        mean_t = (
            round_half_up(sum_t / count)
            if count > 0
            else round_half_up(sum_t)
        )

        print(
            f"{station};{min_t:.1f};{mean_t};{max_t:.1f}"
        )


def main() -> None:
    """Точка входа программы."""

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    if len(sys.argv) < 2:
        sys.stderr.write(
            "Ошибка: не указан путь к файлу.\n"
        )
        sys.stderr.write(
            "Использование: python main.py <путь_к_файлу>\n"
        )
        sys.exit(1)

    file_path = sys.argv[1]

    stations = process_measurements(file_path)
    print_results(stations)


if __name__ == "__main__":
    main()