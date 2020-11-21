# Simple Python Port Scanner

Another python port scanner, nothing special about this one

Install with install.sh debian/red hat based distros
`sudo ./install.sh`

Requirements
`python3`
`python3-pip`
`python3-setuptools`
`argparse`

### Syntax

Specify the address by add in the same line as spps.py

`./sppscan ipv4_address`

Also, port number can be sepecified with ':xx' at the end of the address

`python3 ./sppscan ipv4_address:port_number`

Optional commands are:

`-p/--port`	specify the port insteed of at the end\
`-u/--udp`	use a UDP scan insteed of default TCP (NOTE: they will provide\
	the same results for now)
