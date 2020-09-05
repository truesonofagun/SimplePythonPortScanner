#!/bin/env python3
"""DocString: Simple port scanner made in python"""

import socket


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


def main():
    """Function for user input"""
    _hostip = input('What IPv4 address:')
    _portip = input('What port:')
    scanner(_hostip, _portip)

if __name__ == '__main__':
    main()
