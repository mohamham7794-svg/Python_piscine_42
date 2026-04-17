

from typing import Protocol
from ex1.data_stream import DataStream
from ex0.data_processor import NumericProcessor, TextProcessor, LogProcessor


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class CSVExport:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        values = [v for _, v in data]
        print("CSV Output:")
        print(",".join(values))


class JSONExport:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("JSON Output:")
        result = {}
        for i, (idx, val) in enumerate(data):
            result[f"item_{idx}"] = val
        print(result)


class PipelineDataStream(DataStream):
    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self.processors:
            extracted = []
            for _ in range(nb):
                try:
                    extracted.append(proc.output())
                except Exception:
                    break
            if extracted:
                plugin.process_output(extracted)


def main() -> None:
    print("=== Code Nexus - Data Pipeline ===\n")

    ds = PipelineDataStream()

    print("Initialize Data Stream...\n")
    ds.print_processors_stats()
    print()

    num = NumericProcessor()
    txt = TextProcessor()
    log = LogProcessor()

    print("Registering Processors\n")

    ds.register_processor(num)
    ds.register_processor(txt)
    ds.register_processor(log)

    stream1 = [
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

    print("Send first batch of data on stream:", stream1, "\n")
    ds.process_stream(stream1)

    ds.print_processors_stats()
    print()

    print("Send 3 processed data from each processor to a CSV plugin:")
    ds.output_pipeline(3, CSVExport())

    print()
    ds.print_processors_stats()
    print()

    stream2 = [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [
            {"log_level": "ERROR", "log_message": "500 server crash"},
            {
                "log_level": "NOTICE",
                "log_message": "Certificate expires in 10 days"
            }
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello",
    ]

    print("Send another batch of data:", stream2, "\n")
    ds.process_stream(stream2)

    ds.print_processors_stats()
    print()

    print("Send 5 processed data from each processor to a JSON plugin:")
    ds.output_pipeline(5, JSONExport())

    print()
    ds.print_processors_stats()


if __name__ == "__main__":
    main()
