#!/bin/env python3
"""
Simple Python Port Scanner: a small project to write a simple port scanner
"""

import socket


def scanner(tcpHost, tcpPort):
    try:
        _s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        _s.connect((tcpHost, int(tcpPort)))
        print('[+]%s/tcp open' % tcpHost)
        _s.close()

    except:
        print('[-]%s/tcp closed' % tcpPort)


def main():
    _hostIP = input('What IPv4 address:')
    _portIP = input('What port:')
    scanner(_hostIP, _portIP)


main()
