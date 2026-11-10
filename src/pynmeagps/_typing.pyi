from datetime import date, time
from typing import Protocol, TypeAlias

NMEAValue: TypeAlias = str | int | float | date | time
PayloadDefinition: TypeAlias = dict[str, str | tuple[int | str, "PayloadDefinition"]]

class ReadableStream(Protocol):
    def read(self, size: int, /) -> bytes: ...

class LineReadableStream(ReadableStream, Protocol):
    def readline(self, size: int, /) -> bytes: ...
