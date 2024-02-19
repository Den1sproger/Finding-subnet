# Finding-subnet

An application that selects the minimum subnet containing the IP address data for a given set of IP addresses.

## The time efficiency of the algorithm
Time efficiency of ***get_min_subnet*** function is **O(n * m)**, where

**n** - number of IP addresses in input list,

**m** - number of bits (32 or 128) in one IP address

## To start
Clone this repository
```
git clone https://github.com/Den1sproger/Finding-subnet.git
```
### 1-st way. Run find_subnet.py

#### Windows
```
# IPv4
python find_subnet.py IPv4.txt 4
# IPv6
python find_subnet.py IPv6.txt 6
```
#### MacOS/Lunix
```
# IPv4
python3 find_subnet.py IPv4.txt 4
# IPv6
python3 find_subnet.py IPv6.txt 6
```

### 2-nd way. Run via makefile
```
# IPv4
make run-ipv4
# IPv6
make run-ipv6
```

### 3-rd way. Run with setuptools
Create package
```
pip install .
```
Run command
```
# IPv4
run-ipv4 IPv4.txt 4
# IPv6
run-ipv6 IPv6.txt 6
```

## Test coverage
In total we have **4 functions**. They take up **65 lines** of code.

The tests are designed only for the function ***get_min_subnet***. It takes **32 lines**.

**test coverage** = 32/65 * 100% = **49.23%**

## Run tests

### 1-st way. Run python command
#### Windows
```
python unittest -v tests.py
```
#### MacOS/linux
```
python3 -m unittest -v tests.py
```
### 2-nd way. Run via makefile
```
make tests
```