# Bundled public API types; runtime wire codecs remain in the adjacent .py file.
from pynmeagps.nmeatypes_core import CH as CH, DE as DE, DT as DT, DTL as DTL, HX as HX, IN as IN, LA as LA, LAD as LAD, LN as LN, LND as LND, ST as ST, TM as TM
from pynmeagps._typing import PayloadDefinition as _PayloadDefinition
NMEA_PAYLOADS_GET: dict[str, _PayloadDefinition]
NMEA_PAYLOADS_GET_UNICORE: dict[str, _PayloadDefinition]
