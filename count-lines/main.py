import logging
import sys
import os
import time


def count_lines(filename):
    """
    Count the number of lines in file. If the file can't be
    opened, it should be treated the same as if it was empty.
    """

    ifile = None
    try:
        ifile = open(filename, "r", encoding="utf-8")
        lines = ifile.readlines()
    except TypeError as exp:
        logging.error(exp)
        return 0
    except IOError as exp:
        logging.error(exp)
        return 0
    except UnicodeDecodeError as exp:
        logging.error(exp)
        return 0
    else:
        # print(lines)
        return len(lines)
    finally:
        if ifile:
            ifile.close()


if len(sys.argv) < 2:
    print("main.py file1 file2 ...")
    exit()

for arg in sys.argv[1:]:
    print(os.path.abspath(arg))
    print(time.ctime(os.path.getctime(arg)))
    print(count_lines(arg))
