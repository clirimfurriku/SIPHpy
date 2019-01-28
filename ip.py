import time
import re
import os
import subprocess
import multiprocessing as mp
import httplib2

def first():
    print(" ")
    print(" ")
    print("            Welcome to IP Header scanner         ")
    print("_______________________________________________")
    print(" Scanner IP Headers Python")
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
    print("       My website is www.bardtech.com.       ")
    print("_______________________________________________")
    print("                Project source link.     ")
    print("    https://github.com/clirimfurriku/SIPHpy ")
    print("_______________________________________________")
    print(" ")
    print("_______________________________________________")
    print(" ")
    locaton = os.getcwd()
    print("After finishing see resylts in " + locaton + "/pld.txt")

def hget(ip, rsp, proxy, sprx, port):
    url = "http://%s" % (ip)
    if proxy == 0:
        proxing = httplib2.Http(timeout=1)
    elif proxy == 1:
        proxing = httplib2.Http(proxy_info=httplib2.ProxyInfo(httplib2.socks.PROXY_TYPE_HTTP, sprx, port),timeout=1)
    http_interface = proxing
    try:
        response, content = http_interface.request(url, method="HEAD")
        print("\r[i] Response status: %d - %s for %s" % (response.status, response.reason, ip), end="")
        rsp.append("[+] " + ip + " Status: " + str(response.status) + " - " + response.reason)
    except httplib2.ServerNotFoundError as e:
        print(e.message)
    except httplib2.socket.error:
        print("\r[i] Response status: Error - Unreachable for %s" % ip, end="")
    except:
        pass
    return rsp


#  how IP is saved a.b.c.d = a[0].a[1].a[2].a[3]
# end IP address ea.eb.ec.ed=a[4].a[5].a[6].a[7]

def ip_calc(a, times):
    ip = []
    thend = 0
    stops = 0
    print('\r[i] Checking from  %d.%d.%d.%d to %d.%d.%d.%d' % (a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7]), end="")
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
        if stops == 50:
            break
        stops += 1
    return a, times, ip, thend


def scaner(ip, proxy, sprx, port, output):
    rsp = []
    while ip:
        rsp = hget(ip[0], rsp, proxy, sprx, port)
        ip.remove(ip[0])
    del ip
    for grsp in rsp:
        print(grsp)
        #subprocess.call('echo %s >> pld.txt' % (grsp), shell=True)
        output.put((rsp))


def get_ip():
    print("_______________________________________________")
    print(" ")
    print("Enter IP adress a.b.c.d-ea.eb.ec.ed")
    print("Example 192.168.10.1-192.168.10.255")
    print(" ")
    b = input("Enter value (start-end): ")
    print(" ")
    print("_______________________________________________")
    b = re.split("\D", b)
    a = []
    for element in b:
        a.append(int(element))
    del b
    print(" ")
    print("Do you want to use proxy?")
    print(" ")
    print("Options")
    print(" ")
    print("0) Do not use proxy")
    print("1) Use proxy")
    print(" ")
    proxy = int(input("Enter Option (0 or 1): "))
    print(" ")
    print("_______________________________________________")
    print("_______________________________________________")
    print(" ")
    if proxy == 1:
        sprx = input("Enter Proxy IP:Port (*.*.*.*:****): ")
        print("_______________________________________________")
        print("_______________________________________________")
        print(" ")
        helper = re.split("\:", sprx)
        sprx = helper[0]
        port = int(helper[1])
    elif proxy == 0:
        sprx = 0
        port = 0
    return a, proxy, sprx, port


def mthrd(a, proxy, sprx, port):
    thend: int = 0
    times: int = 1
    b = a
    t = []
    output = mp.Queue()
    whi = 0
    while thend == 0:
        (a, times, ip, thend) = ip_calc(a, times)
        t.append(mp.Process(target=scaner, args=(ip, proxy, sprx, port, output)))
    for thred in t:
        thred.start()
        if whi == 100:
            time.sleep(30)
            whi = 0
        whi += 1
    for thred in t:
        if thred.is_alive():
            thred.join(timeout=2)
    finished = 0
    while finished==0:
        if 'started' in mp.active_children():
            print('\rWorking |', end="")
            time.sleep(0.1)
            print('\rWorking /', end="")
            time.sleep(0.1)
            print('\rWorking -', end="")
            time.sleep(0.1)
            print('\rWorking \\', end="")
            time.sleep(0.1)
        else:
            finished = 1
            print('\rDone!     ', end="")
            time.sleep(1)
    print("Finished")
    results = [output.get() for p in t]
    subprocess.call('echo ____________________________ >> pld.txt', shell=True)
    subprocess.call('echo ___________SIPHpy___________ >> pld.txt', shell=True)
    subprocess.call('echo ____________________________ >> pld.txt', shell=True)
    subprocess.call('echo _________Created By:________ >> pld.txt', shell=True)
    subprocess.call('echo _______Clirim Furriku_______ >> pld.txt', shell=True)
    subprocess.call('echo ____________________________ >> pld.txt', shell=True)
    subprocess.call('echo Checking from  %d.%d.%d.%d to %d.%d.%d.%d >> pld.txt' %
                                 (b[0], b[1], b[2], b[3], b[4], b[5], b[6], b[7]), shell=True)
    subprocess.call('echo ____________________________ >> pld.txt', shell=True)
    subprocess.call('echo __________Results:__________ >> pld.txt', shell=True)
    subprocess.call('echo ____________________________ >> pld.txt', shell=True)
    for result in results:
        for ip in result:
            print(ip)
            subprocess.call('echo %s >> pld.txt' % (ip), shell=True)
    return times


def main():
    (a, proxy, sprx, port) = get_ip()
    start = time.time()
    times = mthrd(a, proxy, sprx, port)
    subprocess.call('echo ____________________________ >> pld.txt', shell=True)
    subprocess.call('echo [i] Checked %d IPs >> pld.txt' % (times), shell=True)
    print('[i] Checked ' + str(times) + ' IPs')
    print("")
    end = time.time()
    took = end - start
    print('[i] Total time to Finish was: ' + str(took))
    subprocess.call('echo [i] Time Taken To Check IPs was %s >> pld.txt' % (took), shell=True)


if __name__ == '__main__':
    first()
    # mp.set_start_method('spawn')
    # mp.get_all_start_methods()
    # mp.freeze_support()
    main()
