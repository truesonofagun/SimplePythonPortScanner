#!/bin/env python3
"""DocString: Simple port scanner made in python"""

import socket
import argparse
import sys


def scanner(tcpHost, tcpPort):
    """This uses a TCP connection to see if port is open
    will info passed through tcpHost and tcpPort var"""
    try:
        _s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        _s.connect((tcpHost, int(tcpPort)))
        print('[+]%s/tcp open' % tcpHost)
        _s.close()

    except:
        print('[-]%s/tcp closed' % tcpPort)


def parserVar():
    parser = argparse.ArgumentParser(description='Simple Python Port Scanner')
    #parser.add_argument('-t', '--tcp', help='preform a TCP port scan', action='store_true', default=False)
    #parser.add_argument('-u', '--udp', help='preform a UDP port scan', action='store_true', default=False)
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
        except e as Exception:
            print(e)

    return parsed


if __name__ == '__main__':
    _c = parserVar()
    _a = _c.address
    _p = _c.port
    scanner(_a, _p)
