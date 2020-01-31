# This script will grep the vsftpd log file to confirm:
# 1) “234 Proceed with negotiation” followed by “SSL version” in the next line.
# 2) “SSL version” and within 4 lines of this we should see either an “OK UPLOAD” or “OK DOWNLOAD"
# Usage: python3 confirm_secure_file_transfer.py <vsftpd log file>

import sys
import subprocess
  

# USER DOES NOT HAVE TO EDIT THIS FILE

if __name__ == '__main__': 
    # TODO - confirm this argument
    retVal = confirm_secure_file_transfer(sys.argv[1])
    print(retVal)
