# Simple Python Port Scanner

Another python port scanner, nothing special about this one

Install with install.sh on distros with apt-get or dnf as package manager\
`sudo ./install.sh`

Requirements\
`python3`\
`python3-pip`\
`python3-setuptools`\
`argparse`\

### Syntax

Specify the address by add in the same line as spps.py

`./sppscan ipv4_address`

Also, port number can be sepecified with ':xx' or ':xx-xx' at the end of the address

`python3 ./sppscan ipv4_address:port_numbers`

Optional commands are:

`-p/--port`	specify the port insteed of at the end\
`-u/--udp`	use a UDP scan insteed of default TCP (NOTE: they will provide\
	the same results for now)
