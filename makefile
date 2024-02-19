run-ipv4:
	python3 find_subnet.py IPv4.txt 4
run-ipv6:
	python3 find_subnet.py IPv6.txt 6
tests:
	python3 -m unittest -v tests.py