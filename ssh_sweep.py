#!/usr/bin/python3
"""
Usage:
  ssh_sweep.py -h | --help
  ssh_sweep.py (--sshpass=<sshpass> --rhosts=<rhosts>) [--sshtimeout=<sshtimeout>] [--sshuser=<sshuser>]
 
Options:
  --sshuser=<sshuser>       Username [default of root]
  --sshpass=<sshpass>       Password 
  --rhosts=<rhosts>         List of targets single ip per line (similar to nmap -iL)
  --sshtimeout=<sshtimeout> Timeout for each ssh attempt [default of 5]
"""

import json
import paramiko
import concurrent.futures

from docopt import docopt


def main():
    opts = docopt(__doc__)


if __name__ == '__main__':
    main()
