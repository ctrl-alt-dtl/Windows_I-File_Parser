# Windows $I File Parser
Quickly parse $I files from Windows Recycle Bin
Used to analyze Windows 7 $I file pulled from the Recycle Bin.


| Data Structure                            | Length in Bytes | Offset to Beginning of Structure |
|-------------------------------------------|-----------------|----------------------------------|
| File Header                               | 8 Bytes         | 0x00                             |
| File Size                                 | 8 Bytes         | From Beginning of File 0x08      |
| File Delete Date and Time                 | 8 Bytes         | From Beginning of File 0x10      |
| File Name and Path (Before Being Deleted) | Up to 520 Bytes | From Beginning of File 0x18      |
