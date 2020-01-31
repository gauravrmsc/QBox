# This script will check if the packet numbers specified indicate zero window are correct. 
# Usage: python3 pcap_check_zero_window.py <packet_numbers_file>

import sys
import os
import re


# USER DOES NOT HAVE TO EDIT THIS FILE

if __name__ == '__main__':
    # TODO - Validate that there is 1 argument
    packet_numbers_filename = sys.argv[1]
    if not os.path.isfile(packet_numbers_filename):
        print('"{}" does not exist'.format(packet_numbers_filename), file=sys.stderr)
        print(False)
        sys.exit(-1)

    retVal = verify_packet_numbers(packet_numbers_filename)
    print(retVal)
    sys.exit(0)
