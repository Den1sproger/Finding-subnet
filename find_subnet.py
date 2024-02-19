import ipaddress
import os
import sys
import argparse



def get_arg_parser() -> argparse.ArgumentParser:
    # get object of parser of CLI arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=str)
    parser.add_argument('ipversion', type=int, choices=(4, 6))

    return parser



def get_data_from_file(filepath: str) -> list[str]:
    # collect data from file with IP addresses
    data = []

    with open(filepath, 'r', encoding='utf-8') as file:
        for line in file:
            data.append(line.strip())

    return data



def get_min_subnet(ip_addresses: list, version: int = 4) -> str:
    if not ip_addresses:
        raise Exception('IP addresses list is empty')
    
    # create list of IPAddresses objects 
    try:
        if version == 4:
            ips = [ipaddress.IPv4Address(ip) for ip in set(ip_addresses)]
        else:
            ips = [ipaddress.IPv6Address(ip) for ip in set(ip_addresses)]
    except ipaddress.AddressValueError:         # if IP addresses is not correct
        raise ValueError("IP addresses don't match the specified version")
    
    # create subnet mask
    binary_ips = ['{:#b}'.format(i)[2:] for i in ips]
    ip_bits_length = len(binary_ips[0])
    ip_count = len(binary_ips)
    mask = 0

    while mask < ip_bits_length:            
        current_chars = [binary_ips[i][mask] for i in range(ip_count)]
        if len(set(current_chars)) == 1:     # if current numbers of adresses are equal
            mask += 1
        else:
            break
    
    # create minimal subnet
    added_zeros = '0' * (ip_bits_length - mask)
    subnet = binary_ips[0][:mask] + added_zeros
    ip = ipaddress.ip_address(int(subnet, 2))

    return f"{ip}/{mask}"




def main() -> None:
    parser = get_arg_parser()
    namespace = parser.parse_args(sys.argv[1:])

    # CLI arguments
    file = namespace.filename
    version = namespace.ipversion

    if not os.path.isfile(file):
        raise FileNotFoundError(f'File {file} not found')

    ip_addresses = get_data_from_file(file)
    subnet = get_min_subnet(ip_addresses, version)
    print(f'Result net: {subnet}')



if __name__ == '__main__':
    main()