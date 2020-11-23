#!/bin/env python3
"""DocString: Simple port scanner made in python"""

import argparse
import sys
from scanner import scanner

def parser_var():
    """Command line syntax created, parsed, and returned"""
    parser = argparse.ArgumentParser(description='Simple Python Port Scanner')
    parser.add_argument('-u', '--udp', help='preform a UDP port scan insteed of default tcp scan', action='store_true', default=False)
    parser.add_argument('-p', '--port', help='given ports for scanning', default=None)
    parser.add_argument('address', help='IPv4 address in format x.x.x.x:xx-xx')

    parsed = parser.parse_args()
    if parsed.port is None:
        try:
            _address = parsed.address.split(':')[0]
            _portstart = parsed.address.split(':')[1]
            try:
                _portend = _portstart.split('-')[1]
                _portstart = _portstart.split('-')[0]
            except IndexError:
                _portstart = _portstart.split('-')[0]
                _portend = None
            parsed.address = _address
            parsed.portStart = _portstart
            parsed.portEnd = _portend
        except IndexError:
            print('Need to specify a port within the address as x.x.x.x:xx-xx\n' +
                    'or with the -p/--port argument')
            sys.exit()
        except Exception as _e:
            print(_e)
    else:
        try:
            _portend = parsed.port.split('-')[1]
            _portstart = parsed.port.split('-')[0]
        except IndexError:
            _portend = None
            _portstart = parsed.port.split('-')[0]
        parsed.portStart = _portstart
        parsed.portEnd = _portend

    return parsed


if __name__ == '__main__':
    _input = parser_var()
    scanner(_input.address, _input.portStart, _input.portEnd, _input.udp)
