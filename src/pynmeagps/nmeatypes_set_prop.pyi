# Bundled public API types; runtime wire codecs remain in the adjacent .py file.
from pynmeagps.nmeatypes_core import CH as CH, DE as DE, DT as DT, HX as HX, IN as IN, LA as LA, LAD as LAD, LN as LN, LND as LND, QS as QS, ST as ST, TM as TM
from pynmeagps.nmeatypes_get_prop import NMEA_PAYLOADS_GET_PROP as NMEA_PAYLOADS_GET_PROP
from pynmeagps._typing import PayloadDefinition as _PayloadDefinition
NMEA_PAYLOADS_SET_PROP: dict[str, _PayloadDefinition]
