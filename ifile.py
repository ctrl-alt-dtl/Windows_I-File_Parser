from struct import unpack
import struct
import binascii
from datetime import datetime as dt
from datetime import timedelta
import string

# Name of the $I file (in this case I have the test case file)
input =  "i-file"

with open(input, 'rb') as headerStruct:
    fileHeader = headerStruct.read(8)

    print("File Header (not needed): " + binascii.hexlify(fileHeader).decode('ascii'))

    # Read 4 bytes at a time to do the file size conversion
    fileSize1 = headerStruct.read(4)
    fileSize2 = headerStruct.read(4)
    result1 = unpack("<I", fileSize1)[0]
    result2 = unpack("<I", fileSize2)[0]
    resultSize = result2 + result1
    print("File Size: " + str(resultSize) + " bytes")

    # Read 8 bytes at a time to do the to create the string for the time conversion
    fileDateTime = headerStruct.read(8)
    # Date/Time as Big Endian hex time of file - unconverted
    dtf = binascii.hexlify(fileDateTime).decode('ascii')

    # Win 64 Hex conversion code used from (https://github.com/Fetchered/time_decode/blob/master/time_decode.py)
    converted_time = struct.unpack("<Q", binascii.unhexlify(dtf))[0]
    # Windows Epoch Time of 01 Jan 1601
    dt_obj = dt(1601, 1, 1) + timedelta(microseconds=converted_time / 10)
    # STRFTIME (https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior)
    finalDTG = dt_obj.strftime('%a %d %B %Y %H:%M:%S %Z')
    print("Date/Time (Windows): " + finalDTG)

    # File path of data without Unicode blocks
    filePath = headerStruct.read(520)
    printable = set(string.printable)
    print("File Path: " + str(filter(lambda x: x in printable, binascii.hexlify(filePath).decode('ascii').decode('hex'))))



