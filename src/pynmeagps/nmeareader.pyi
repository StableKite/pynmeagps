# Bundled public API types; runtime wire codecs remain in the adjacent .py file.
from logging import getLogger as getLogger
from socket import socket as socket
from types import NoneType as NoneType
from typing import Callable as Callable, Literal as Literal
from pynmeagps.nmeahelpers import calc_checksum as calc_checksum, get_parts as get_parts
from pynmeagps.nmeamessage import NMEAMessage as NMEAMessage
from pynmeagps.nmeatypes_core import DEFAULT_BUFSIZE as DEFAULT_BUFSIZE, ENCODE_NONE as ENCODE_NONE, ERR_LOG as ERR_LOG, ERR_RAISE as ERR_RAISE, GET as GET, MAXBUFSIZE as MAXBUFSIZE, NMEA_HDR as NMEA_HDR, VALCKSUM as VALCKSUM, VALMSGID as VALMSGID
from pynmeagps.socketwrapper import SocketWrapper as SocketWrapper
from collections.abc import Callable as _Callable
from typing import Literal as _Literal
from pynmeagps._typing import LineReadableStream as _LineReadableStream, PayloadDefinition as _PayloadDefinition
class NMEAReader:
    def __init__(self, stream: _LineReadableStream | socket, msgmode: _Literal[0, 1, 2] = ..., validate: int = ..., nmeaonly: bool = ..., quitonerror: _Literal[0, 1, 2] = ..., bufsize: int = ..., errorhandler: _Callable[[Exception], object] | None = ..., userdefined: dict[str, _PayloadDefinition] | None = ..., encoding: int = ...) -> None: ...
    def __iter__(self) -> NMEAReader: ...
    def __next__(self) -> tuple[bytes | None, NMEAMessage | None]: ...
    def read(self) -> tuple[bytes | None, NMEAMessage | None]: ...
    @property
    def datastream(self) -> _LineReadableStream: ...
    @staticmethod
    def parse(message: bytes | str, msgmode: _Literal[0, 1, 2] = ..., validate: int = ..., userdefined: dict[str, _PayloadDefinition] | None = ...) -> NMEAMessage | None: ...

