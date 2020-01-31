# This script will check if the packet number specified as the initiation of abnormal termination is correct.
# Usage: python3 pcap_check_connection_termination.py <packet_numbers_file>

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
