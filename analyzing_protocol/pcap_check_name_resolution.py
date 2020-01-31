# This script will check if the packet numbers specified in one file are
# Domain Name Resolution related packets in another pcap file.
# Usage: python3 pcap_check_name_resolution.py <pcap_file> <packet_numbers_file>

import sys
from scapy.utils import rdpcap
from scapy.layers.dns import DNSRR, DNS, DNSQR


# USER DOES NOT HAVE TO EDIT THIS FILE

if __name__ == '__main__':
    # TODO - Validate that there are 2 arguments
    pcap_filename = sys.argv[1]
    packet_numbers_filename = sys.argv[2]
    if not os.path.isfile(pcap_filename):
        print('"{}" does not exist'.format(pcap_filename), file=sys.stderr)
        print(False)
        sys.exit(-1)

    if not os.path.isfile(packet_numbers_filename):
        print('"{}" does not exist'.format(packet_numbers_filename), file=sys.stderr)
        print(False)
        sys.exit(-1)

    retVal = process_pcap(pcap_filename, packet_numbers_filename)
    print(retVal)
    sys.exit(0)
