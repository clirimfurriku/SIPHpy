import time
import re
import httplib2
import subprocess
import os
import multiprocessing as mp


# Lest begin

def first():
    print(" ")
    print(" ")
    print("           Welcome to IP Header scanner        ")
    print("_______________________________________________")
    print("            Scanner IP Headers Python          ")
    print("_______________________________________________")
    print(" ")
    print("    .--. .-..---. .-..-.             ")
    print("   : .--': :: .; :: :; :             ")
    print("   `. `. : ::  _.':    :.---. .-. .-.")
    print("    _`, :: :: :   : :: :: .; `: :_; :")
    print("   `.__.':_;:_;   :_;:_;: ._.'`._ . :")
    print("                        : :     .-' ;")
    print("                        :_;     `--' ")
    print(" ")
    print("This application is developed by Clirim Furriku")
    print(" ")
    print("               Never change my name            ")
    print("_______________________________________________")
    print("        My website is www.bardtech.com         ")
    print("_______________________________________________")
    print("                Project source link.           ")
    print("    https://github.com/clirimfurriku/SIPHpy    ")
    print("_______________________________________________")
    print(" ")
    print("_______________________________________________")
    print(" ")
    locaton = os.getcwd()
    print("After finishing see results in " + locaton + "\pld.txt")


def hget(ip, rsp, proxy, set_proxy, port):
    url = "http://%s" % ip
    if proxy == 0:
        proxing = httplib2.Http(timeout=1)
    elif proxy == 1:
        proxing = httplib2.Http(proxy_info=httplib2.ProxyInfo(httplib2.socks.PROXY_TYPE_HTTP_NO_TUNNEL, set_proxy, port),
                                timeout=1)
    http_interface = proxing
    try:
        response, content = http_interface.request(url, method="HEAD")
        print("\r[i] Response status: %d - %s for %s" % (response.status, response.reason, ip), end="")
        rsp.append("[+] " + ip + " Status: " + str(response.status) + " - " + response.reason)
    except httplib2.ServerNotFoundError as e:
        print(e.message)
    except httplib2.socket.error:
        print("\r[i] Response status: Error - Unreachable for %s" % ip, end="")
    except httplib2.httplib.ResponseNotReady:
        pass
    return rsp


#  how IP is saved a.b.c.d = a[0].a[1].a[2].a[3]
# end IP address ea.eb.ec.ed=a[4].a[5].a[6].a[7]

def ip_calc(a, times):
    ip = []
    thend = 0
    stops = 0
    print('\r[i] Calculating  %d.%d.%d.%d to %d.%d.%d.%d' % (a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7]), end="")
    ip.append('%d.%d.%d.%d' % (a[0], a[1], a[2], a[3]))
    if a[0] > 255 or a[1] > 255 or a[2] > 255 or a[3] > 255:
        thend = 1
    while a[0] <= 255 or a[1] <= 255 or a[2] <= 255 or a[3] <= 255:
        if a[0] >= a[4] and a[1] >= a[5] and a[2] >= a[6] and a[3] >= a[7]:
            thend = 1
            break
        a[3] += 1
        if a[3] >= 255:
            a[2] += 1
            a[3] = 0
        if a[2] >= 255:
            a[1] += 1
            a[2] = 0
        if a[1] >= 255:
            a[0] += 1
            a[1] = 0
        if a[0] >= 255:
            break
        times += 1
        ip.append('%d.%d.%d.%d' % (a[0], a[1], a[2], a[3]))
        if stops == 100:
            break
        stops += 1
    return a, times, ip, thend


def scaner(ip, proxy, sprx, port):
    rsp = []
    for adress in ip:
        rsp = hget(adress, rsp, proxy, sprx, port)
    return rsp


def get_ip():
    print("_______________________________________________")
    print(" ")
    print("Enter IP address a.b.c.d-ea.eb.ec.ed")
    print("Example 192.168.10.1-192.168.10.255")
    print(" ")
    try:
        b = input("Enter value (start-end): ")
    except:
        print("[!] Wrong Value")
        print("Enter IP address a.b.c.d-ea.eb.ec.ed")
        print("Example 192.168.10.1-192.168.10.255")
        b = input("Enter value (start-end): ")
    while b != re.search("(\d*\D\d*\D\d*\D\d*\D\d*\D\d*\D\d*\D\d)", b ).group(0):
        print("\n\nYour Value is wrong")
        print("Please enter ip as in example")
        print("Example 192.168.10.1-192.168.10.255")
        try:
            b = input("Enter value (start-end): ")
        except:
            print("[!] Wrong Value")
            print("Enter IP address a.b.c.d-ea.eb.ec.ed")
            print("Example 192.168.10.1-192.168.10.255")
            b = input("Enter value (start-end): ")
    print(" ")
    print("_______________________________________________")
    b = re.split("\D", b)
    a = []
    for element in b:
        a.append(int(element))
    del b
    print(" ")
    print("How many threads do you want to use?")
    print(" ")
    print("Recommended 50")
    print(" ")
    try:
        threads = int(input("Enter MAX number of threads to use: "))
    except ValueError:
        threads = 50
    print(" ")
    print("_______________________________________________")
    print(" ")
    print("Do you want to use proxy?")
    print(" ")
    print("Options")
    print(" ")
    print("0) Do not use proxy")
    print("1) Use proxy")
    print(" ")
    try:
        proxy = int(input("Enter Option (0 or 1): "))
    except ValueError:
        proxy = 0
    while proxy is not 1 and proxy is not 0:
        print("Wrong Option")
        try:
            proxy = int(input("Enter Option (0 or 1): "))
        except ValueError:
            pass
    print(" ")
    print("_______________________________________________")
    print("_______________________________________________")
    print(" ")
    if proxy == 1:
        set_proxy = input("Enter Proxy IP:Port (*.*.*.*:****): ")
        while set_proxy != re.search("(\d*\D\d*\D\d*\D\d*\D\d*)", set_proxy ).group(0):
            print("Wrong value of proxy")
            set_proxy = input("Enter Proxy IP:Port (*.*.*.*:****): ")
        helper = re.split("\:", set_proxy)
        set_proxy = helper[0]
        port = int(helper[1])
    elif proxy == 0:
        set_proxy = 0
        port = 0
    return a, proxy, set_proxy, port, threads


def mthrd(a, proxy, sprx, port, threads):
    b = a
    print("Starting " + str(threads) + " Threads")
    pool = mp.Pool(processes=threads)
    print("Threads started")
    thend: int = 0
    times: int = 1
    t = []
    while thend == 0:
        (a, times, ip, thend) = ip_calc(a, times)
        t.append(ip)
    time.sleep(5)
    results = [pool.apply_async(scaner, args=(ipd, proxy, sprx, port,)) for ipd in t]
    output = [p.get() for p in results]
    subprocess.call('echo ____________________________ >> pld.txt', shell=True)
    subprocess.call('echo ___________SIPHpy___________ >> pld.txt', shell=True)
    subprocess.call('echo ____________________________ >> pld.txt', shell=True)
    subprocess.call('echo _________Created By:________ >> pld.txt', shell=True)
    subprocess.call('echo _______Clirim Furriku_______ >> pld.txt', shell=True)
    subprocess.call('echo ____________________________ >> pld.txt', shell=True)
    subprocess.call('echo Checking from  %d.%d.%d.%d to %d.%d.%d.%d >> pld.txt' % (b[0], b[1], b[2], b[3], b[4], b[5], b[6], b[7]), shell=True)
    subprocess.call('echo ____________________________ >> pld.txt', shell=True)
    subprocess.call('echo __________Results:__________ >> pld.txt', shell=True)
    subprocess.call('echo ____________________________ >> pld.txt', shell=True)
    for success in output:
        for individual_ip in success:
            if individual_ip:
                subprocess.call('echo %s >> pld.txt' % individual_ip, shell=True)
                print(individual_ip)
    return times


def main():
    (a, proxy, set_proxy, port, threads) = get_ip()
    start = time.time()
    times = mthrd(a, proxy, set_proxy, port, threads)
    subprocess.call('echo ____________________________ >> pld.txt', shell=True)
    subprocess.call('echo [i] Checked %d IPs >> pld.txt' % times, shell=True)
    print('\n\n[i] Checked ' + str(times) + ' IPs')
    print("")
    end = time.time()
    took = end - start
    print('[i] Total time to Finish was: ' + str(took))
    subprocess.call('echo [i] Time Taken To Check IPs was %s seconds >> pld.txt' % took, shell=True)


if __name__ == '__main__':
    first()
    # mp.set_start_method('spawn')
    # mp.set_start_method('forkserver')
    # mp.set_start_method('fork')
    # mp.freeze_support()
    main()
