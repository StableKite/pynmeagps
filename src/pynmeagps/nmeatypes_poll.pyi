# Bundled public API types; runtime wire codecs remain in the adjacent .py file.
from pynmeagps.nmeatypes_core import ST as ST
from pynmeagps._typing import PayloadDefinition as _PayloadDefinition
NMEA_PAYLOADS_POLL: dict[str, _PayloadDefinition]
