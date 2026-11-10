The wheel and source distribution include complete adjacent public API stubs
and the PEP 561 marker. Runtime codec modules are unchanged except for the
distribution version. No error-code, validation, stream or payload behavior
is changed by this typing delivery.

Reader streams are structural binary read(size) protocols. NMEA and mixed UBX
readers additionally require readline(size); socket.socket is accepted through
the existing SocketWrapper. Callback arguments, parser modes, raw payloads,
serialization, conversions and exported protocol tables have explicit types.
NMEA values include empty strings, numbers, date and time; UBX values include
byte strings and integer arrays. Dynamic message fields expose these bounded
unions rather than Any. Narrow a field to the expected runtime type before
using type-specific operations. Parsing disabled or metadata-only reader modes
can return None or strings, as the existing runtime actually does.

Install the coordinated three-package typing set when consuming UBX or RTCM
interfaces; their original runtime dependency constraints are unchanged.
No static-checker suppressions or runtime code substitutions are required.

The existing pyrtcm 1.2.1 RTCM1072 groupsig3_grp definition contains a set[str]
where the parser ordinarily expects a dictionary. Its actual exported data type
is represented honestly; this typing change does not repair that codec entry.
