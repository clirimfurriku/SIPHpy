# !/usr/bin/env python3
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from time import time
import os

PROXY = 'http://1.1.1.1:80'
TIMEOUT = 40
VERBOSE = False


class IPAddress:
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
        self.end_a = 255
        self.end_b = 255
        self.end_c = 255
        self.end_d = 255

    def set_end(self, end_a, end_b, end_c, end_d):
        self.end_a = int(end_a)
        self.end_b = int(end_b)
        self.end_c = int(end_c)
        self.end_d = int(end_d)

    def set_subnet(self, subnet):
        return 'Not implemented'

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
        return f'<IP_Address Start: {self.a}.{self.b}.{self.c}.{self.d}  ' \
               f'End: {self.end_a}.{self.end_b}.{self.end_c}.{self.end_d}>'

    def end_ip(self):
        return f'{self.end_a}.{self.end_b}.{self.end_c}.{self.end_d}'


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
print('IP Example 192.168.1.1')
ip_start = input('Please Enter start IP: ').split('.')
ip_end = input('Please Enter end IP: ').split('.')

ip = IPAddress(*ip_start)
if len(ip_end) == 4:
    ip.set_end(*ip_end)

responses = []
start = time()
with ThreadPoolExecutor(max_workers=(os.cpu_count() or 1) * 50) as executor:
    for i in executor.map(scan, ip):
        if i:
            responses.append(i)
            print(i)

end = time()
took = end - start

print(f'It took {took} to scan IPs from {ip} to {ip.end_ip}')

with open('results.txt', 'w') as file:
    for i in responses:
        file.write(str(i))
