#!/bin/env python3
"""The python scanner logic"""

import socket
import sys

def scanner(_addr, _portstart, _portend, _udp):
    """this passes the paramiters into the scan_logic and enumerate port in a given
    range based if the _portend is not None"""
    if _portend is None:
        scan_logic(_addr, _portstart, _udp)
    else:
        _portend = int(_portend) + 1
        for i in range(int(_portstart), _portend):
            scan_logic(_addr, i, _udp)



def scan_logic(_addr, _port, _udp):
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
