

from typing import Any
from ex0.data_processor import (
    DataProcessor,
    NumericProcessor,
    TextProcessor,
    LogProcessor,
)


class DataStream:
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for item in stream:
            handled: bool = False
            for proc in self.processors:
                if proc.validate(item):
                    proc.ingest(item)
                    handled = True
                    break
            if not handled:
                print(
                    "DataStream error - Can't process element "
                    f"in stream: {item}"
                )

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self.processors:
            print("No processor found, no data")
            return

        for proc in self.processors:
            print(
                f"{proc.__class__.__name__}: total "
                f"{proc._total_processed} items "
                f"processed, remaining {len(proc._data)} on processor"
            )


def main() -> None:
    print("=== Code Nexus - Data Stream ===\n")

    ds = DataStream()

    print("Initialize Data Stream...")
    ds.print_processors_stats()
    print()

    num = NumericProcessor()

    print("Registering Numeric Processor\n")
    ds.register_processor(num)

    stream = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                "log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead"
            },
            {
                "log_level": "INFO",
                "log_message": "User wil is connected"
            }
        ],
        42,
        ["Hi", "five"],
    ]

    print("Send first batch of data on stream:", stream, "\n")
    ds.process_stream(stream)

    ds.print_processors_stats()
    print()

    print("Registering other data processors\n")

    txt = TextProcessor()
    log = LogProcessor()

    ds.register_processor(txt)
    ds.register_processor(log)

    print("Send the same batch again")
    ds.process_stream(stream)

    ds.print_processors_stats()
    print()

    print(
        "Consume some elements from the data processors: "
        "Numeric 3, Text 2, Log 1"
    )

    for _ in range(3):
        num.output()
    for _ in range(2):
        txt.output()
    for _ in range(1):
        log.output()

    ds.print_processors_stats()


if __name__ == "__main__":
    main()
