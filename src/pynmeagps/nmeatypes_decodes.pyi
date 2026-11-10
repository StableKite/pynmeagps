# Bundled public API types; runtime wire codecs remain in the adjacent .py file.
FIXTYPE_GGA: dict[int, str]
QUALITY: dict[int, str]
POSMODE: dict[str, str]
GNSSLIST: dict[int, str]
SYSTEMID: dict[str, str]
SIGNALID: dict[tuple[str, str], str]
FMI_STATUS: dict[int, tuple[str, str]]
