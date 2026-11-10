# Bundled public API types; runtime wire codecs remain in the adjacent .py file.
from pynmeagps._typing import PayloadDefinition as _PayloadDefinition
NMEA_PAYLOADS_SET: dict[str, _PayloadDefinition]
