#!/bin/env python3
"""DocString: Simple port scanner made in python"""

import argparse
import sys
from scanner import scanner

def parser_var():
    """Command line syntax created, parsed, and returned"""
    parser = argparse.ArgumentParser(description='Simple Python Port Scanner')
    parser.add_argument('-u', '--udp', help='preform a UDP port scan insteed of default tcp scan', action='store_true', default=False)
    parser.add_argument('-p', '--port', help='given port for scanning', type=int, default=None)
    parser.add_argument('address', help='IPv4 address in format x.x.x.x:xx')

    parsed = parser.parse_args()
    if parsed.port is None:
        try:
            _address = parsed.address.split(':')[0]
            _port = parsed.address.split(':')[1]
            parsed.address = _address
            parsed.port = _port
        except IndexError:
            print('Need to specify a port within the address as x.x.x.x:xx\n' +
                    'or with the -p/--port argument')
            sys.exit()
        except Exception as _e:
            print(_e)

    return parsed


if __name__ == '__main__':
    _input = parser_var()
    scanner(_input.address, _input.port, _input.udp)
