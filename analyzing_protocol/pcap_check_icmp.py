# This script will check if the IP address specified in one file is present
# as the Destination IP of the ICMP Request packets in another pcap file.
# Usage: python3 pcap_check_icmp.py <pcap_file> <server_ip_file>

import sys
from scapy.utils import rdpcap
from scapy.layers.inet import IP, ICMP


# USER DOES NOT HAVE TO EDIT THIS FILE

if __name__ == '__main__':
    # TODO - Validate that there are 2 arguments
    pcap_filename = sys.argv[1]
    server_ip_filename = sys.argv[2]
    if not os.path.isfile(pcap_filename):
        print('"{}" does not exist'.format(pcap_filename), file=sys.stderr)
        print(False)
        sys.exit(-1)

    if not os.path.isfile(server_ip_filename):
        print('"{}" does not exist'.format(server_ip_filename), file=sys.stderr)
        print(False)
        sys.exit(-1)

    retVal = process_pcap(pcap_filename, server_ip_filename)
    print(retVal)
    sys.exit(0)
