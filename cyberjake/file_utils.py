
import os
import codecs


def remove_bom_inplace(path: str):
    """
    Removes BOM mark, if it exists, from a file and rewrites it in-place.
    :param path: Path to the file. Works with anything to use for open()
    """
    buffer_size = 4096
    bom_length = len(codecs.BOM_UTF8)

    with open(path, "rb") as fp:
        chunk = fp.read(buffer_size)
        if chunk.startswith(codecs.BOM_UTF8):
            i = 0
            chunk = chunk[bom_length:]
            while chunk:
                fp.seek(i)
                fp.write(chunk)
                i += len(chunk)
                fp.seek(bom_length, os.SEEK_CUR)
                chunk = fp.read(buffer_size)
            fp.seek(-bom_length, os.SEEK_CUR)
            fp.truncate()
