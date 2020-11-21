#!/bin/env python3
"""The python scanner logic"""

import socket
import sys

def scanner(_addr, _port, _udp):
    """This uses a TCP (or UDP if specified) connection to see if port is open
    will info passed through addr and port var"""
    if _udp is True:
        _type = socket.SOCK_DGRAM
        _name = 'udp'

    else:
        _type = socket.SOCK_STREAM
        _name = 'tcp'

    try:
        _s = socket.socket(socket.AF_INET, _type)
        _s.connect((_addr, int(_port)))
        print('[+]%s:%s/%s open' % (_addr,_port,_name))
        _s.close()

    except KeyboardInterrupt:
        sys.exit()

    except ConnectionRefusedError:
        print('[-]%s:%s/%s closed' % (_addr,_port,_name))

    except ConnectionAbortedError:
        print('The connection has been severed')
        sys.exit()

    except OSError as _e:
        print(_e)


