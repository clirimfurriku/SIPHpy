# !/usr/bin/env python3
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from time import time
import os

PROXY = 'http://1.1.1.1:80'
TIMEOUT = 40
VERBOSE = False


class Network:
    def __init__(self, a=1, b=1, c=1, d=1):
        """
        192.168.0.100
         a . b .c. d
        :param a: First 8 Bit
        :param b: Next 8 Bit
        :param c: Next 8 Bit
        :param d: Last 8 Bit
        """

        self.a = int(a)
        self.b = int(b)
        self.c = int(c)
        self.d = int(d)
        self.start_a = int(a)
        self.start_b = int(b)
        self.start_c = int(c)
        self.start_d = int(d)
        self.end_a = 255
        self.end_b = 255
        self.end_c = 255
        self.end_d = 255

    def set_end(self, end_a, end_b, end_c, end_d):
        self.end_a = int(end_a)
        self.end_b = int(end_b)
        self.end_c = int(end_c)
        self.end_d = int(end_d)

    def set_subnet(self, subnet_mask):
        """
        :param subnet_mask: Number of network bits (0-31), type: int
        """
        subnet_mask = int(subnet_mask)
        sub_a = ''
        sub_b = ''
        sub_c = ''
        sub_d = ''
        byte = 0
        while byte < 32:
            if 0 <= byte <= 7:
                if byte < subnet_mask:
                    sub_a += '0'
                else:
                    sub_a += '1'
            elif 8 <= byte <= 15:
                if byte < subnet_mask:
                    sub_b += '0'
                else:
                    sub_b += '1'
            elif 16 <= byte <= 23:
                if byte < subnet_mask:
                    sub_c += '0'
                else:
                    sub_c += '1'
            elif 24 <= byte <= 31:
                if byte < subnet_mask:
                    sub_d += '0'
                else:
                    sub_d += '1'
            byte += 1
        self.end_a = int(sub_a, 2) | self.start_a
        self.end_b = int(sub_b, 2) | self.start_b
        self.end_c = int(sub_c, 2) | self.start_c
        self.end_d = int(sub_d, 2) | self.start_d

    def __iter__(self):
        return self

    def __next__(self):
        self.d += 1
        if self.d > 255:
            self.d = 0
            self.c += 1
            if self.c > 255:
                self.c = 0
                self.b += 1
                if self.b > 255:
                    self.b = 0
                    self.a += 1
                    if self.a > 255:
                        raise StopIteration
        if self.a == self.end_a and self.b == self.end_b and self.c == self.end_c and self.d == self.end_d:
            raise StopIteration
        return f'{self.a}.{self.b}.{self.c}.{self.d}'

    def __gt__(self, other):
        return self.a > other.a and self.b > other.b and self.c > other.c and self.d > other.d

    def __lt__(self, other):
        return self.a < other.a and self.b < other.b and self.c < other.v and self.d < other.d

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b and self.c == other.c and self.d == other.d

    def __str__(self):
        return f'{self.a}.{self.b}.{self.c}.{self.d}'

    def __repr__(self):
        return f'<Network Start: {self.start_a}.{self.start_b}.{self.start_c}.{self.start_d}  ' \
               f'End: {self.end_a}.{self.end_b}.{self.end_c}.{self.end_d}>'

    def __len__(self):
        return (self.end_a - self.start_a or 1) * (self.end_b - self.start_b or 1) * \
               (self.end_c - self.start_c or 1) * (self.end_d - self.start_d or 1)

    @property
    def end_ip(self):
        return f'{self.end_a}.{self.end_b}.{self.end_c}.{self.end_d}'

    @property
    def start_ip(self):
        return f'{self.start_a}.{self.start_b}.{self.start_c}.{self.start_d}'

    def reset(self):
        self.a = self.start_a
        self.b = self.start_b
        self.c = self.start_c
        self.d = self.start_d


def scan(ip_host):
    print(f'\r{ip_host}', end='')

    proxy_support = urllib.request.ProxyHandler({'http': PROXY,
                                                 'https': PROXY})
    opener = urllib.request.build_opener(proxy_support)
    urllib.request.install_opener(opener)

    try:
        response = urllib.request.urlopen('http://' + ip_host, timeout=TIMEOUT)
        return [ip_host, response]
    except urllib.error.HTTPError as e:
        return [ip_host, e]
    except Exception as e:
        if VERBOSE:
            print(e)
        return


def first():
    print("                                       ")
    print("                                       ")
    print("     Welcome to IP Header scanner      ")
    print(" _____________________________________ ")
    print("        Scanner IP Headers Python      ")
    print(" _____________________________________ ")
    print("                                       ")
    print("     .--. .-..---. .-..-.              ")
    print("    : .--': :: .; :: :; :              ")
    print("    `. `. : ::  _.':    :.---. .-. .-. ")
    print("     _`, :: :: :   : :: :: .; `: :_; : ")
    print("    `.__.':_;:_;   :_;:_;: ._.'`._ . : ")
    print("                         : :     .-' ; ")
    print("                         :_;     `--'  ")
    print("                                       ")
    print("   This application is developed by:   ")
    print("                        Clirim Furriku ")
    print("                                       ")
    print(" _____________________________________ ")
    print("                                       ")
    print(" _____________________________________ ")
    print("          Project source link:         ")
    print("https://github.com/clirimfurriku/SIPHpy")
    print(" _____________________________________ ")
    print("                                       ")
    print(" _____________________________________ ")
    print("                                       ")


first()
print('IP Example: 192.168.1.1/24')
ip_start = input('Please Enter start IP: ').split('.')
if len(ip_start[-1].split('/')) == 2:
    subnet = ip_start[-1].split('/')[1]
    ip_start[-1] = ip_start[-1].split('/')[0]
    ip = Network(*ip_start)
    ip.set_subnet(subnet)
else:
    ip_end = input('Please Enter last IP of the network: ').split('.')
    ip = Network(*ip_start)
    ip.set_end(*ip_end)


print(f'Total number of IPs on the network is {len(ip)}')
responses = []
start = time()
with ThreadPoolExecutor(max_workers=(os.cpu_count() or 1) * 50) as executor:
    for i in executor.map(scan, ip):
        if i:
            responses.append(i)
            print(f'{i}')

end = time()
took = end - start

print(f'It took {took} to scan IPs from {ip.start_ip} to {ip.end_ip}')

print('\nSaving results...')
with open('results.txt', 'w') as file:
    for i in responses:
        file.write(str(i))
    print(f'Results saved as results.txt at location {os.getcwd()}')
