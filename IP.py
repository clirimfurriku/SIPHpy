import threading
import httplib2
from time import sleep, time

proxy = 0
proxy_ip = '185.35.67.207'
port = 8080
num_of_ip_for_thread = 1
finished = False


def back_calc(ip_to_calc):
    global finished
    list_of_ip_calculated = []
    i = 0
    if (ip_to_calc[0] >= ip_to_calc[4] and ip_to_calc[1] >= ip_to_calc[5] and
            ip_to_calc[2] >= ip_to_calc[6] and ip_to_calc[3] >= ip_to_calc[7]):
        finished = True
        return ip_to_calc
    while i < num_of_ip_for_thread and (ip_to_calc[0] < ip_to_calc[4] or ip_to_calc[1] < ip_to_calc[5] or
                                        ip_to_calc[2] < ip_to_calc[6] or ip_to_calc[3] < ip_to_calc[7]):
        i += 1
        ip_to_calc[3] += 1
        if ip_to_calc[3] > 255:
            ip_to_calc[2] += 1
            ip_to_calc[3] = 0
        if ip_to_calc[2] > 255:
            ip_to_calc[1] += 1
            ip_to_calc[2] = 0
        if ip_to_calc[1] > 255:
            ip_to_calc[0] += 1
            ip_to_calc[1] = 0
        if ip_to_calc[0] > 255:
            list_of_ip_calculated.append(
                str(ip_to_calc[0]) + '.' + str(ip_to_calc[1]) + '.' + str(ip_to_calc[2]) + '.' + str(ip_to_calc[3]))
            start_thread(list_of_ip_calculated)
            return ip_to_calc
        if i == num_of_ip_for_thread:
            list_of_ip_calculated.append(
                str(ip_to_calc[0]) + '.' + str(ip_to_calc[1]) + '.' + str(ip_to_calc[2]) + '.' + str(ip_to_calc[3]))
            start_thread(list_of_ip_calculated)
            return ip_to_calc
        list_of_ip_calculated.append(
            str(ip_to_calc[0]) + '.' + str(ip_to_calc[1]) + '.' + str(ip_to_calc[2]) + '.' + str(ip_to_calc[3]))
    if len(list_of_ip_calculated) < 1:
        return ip_to_calc
    start_thread(list_of_ip_calculated)
    return ip_to_calc


def start_thread(ip_list):
    thread = threading.Thread(target=do_scan, args=ip_list)
    thread.start()


def get_header(ip_address):
    poxing = httplib2.Http(timeout=1)
    if proxy == 1:
        poxing = httplib2.Http(proxy_info=httplib2.ProxyInfo(httplib2.socks.PROXY_TYPE_HTTP, proxy_ip, port),
                               timeout=1)
    http_interface = poxing
    try:
        response, content = http_interface.request(ip_address, method="HEAD")
        print("\r[i] Response status: {} - {} for {}".format(response.status, response.reason, ip_address))
    except httplib2.ServerNotFoundError:
        pass
        # print('\rUnable to resolve the host {}.'.format(ip_address), end="")
    except httplib2.socket.error:
        pass
        # print("\r[i] Response status: Error - Unreachable for {} ".format(ip_address), end="")
    except httplib2.RedirectLimit:
        print("\r[i] Response status: redirection_limit - Too many redirects for {} ".format(ip_address))
    except httplib2.MalformedHeader:
        print("\r[i] Response status: UNKNOWN Header - WWW-Authenticate for {} ".format(ip_address))
    except httplib2.socks.HTTPError as e:
        if 'Forbidden' in str(e.args):
            print("\r[i] Response status: Error - Forbidden for {} ".format(ip_address))
        else:
            print(e.args)
    # except:
    #     print("\r[i] Unknown error for {} ".format(ip_address), end="")
    #     pass


def calculate_thread(ip_to_split, threads_to_split):
    # 1.1.1.1-2.1.1.1 = (2-1)*(255^3)+(1-1)*(255^2)+(1-1)*(255) + 1-1
    # 2-1 = 1 * 255 * 255  * 255 =
    # ip_to_split = [1, 1, 1, 1, 2, 1, 1, 1]
    #                0, 1, 2, 3, 4, 5, 6, 7
    total_num_of_ips = (ip_to_split[4] - ip_to_split[0]) * (255 ** 3) + \
                       (ip_to_split[5] - ip_to_split[1]) * (255 ** 2) + \
                       (ip_to_split[6] - ip_to_split[2]) * 255 + \
                       (ip_to_split[7] - ip_to_split[3])
    print('Total number of IP to Scan', total_num_of_ips)
    num_of_ip_for_a_thread = int(total_num_of_ips / threads_to_split)
    while total_num_of_ips - float(num_of_ip_for_a_thread * threads_to_split) > threads_to_split:
        num_of_ip_for_a_thread += 1
    print('There will be {} IPs scanned for thread'.format(num_of_ip_for_a_thread + 1))
    return num_of_ip_for_a_thread, total_num_of_ips


def do_scan(*args):
    if (len(args)) == 0:
        return
    for ip_to_scan in args:
        address = 'http://' + ip_to_scan
        get_header(address)
        # print(address)


# get_header(address)


def first():
    print(" ")
    print(" ")
    print("    Welcome to IP Header scanner     ")
    print("_______________________ _____________")
    print("       Scanner IP Headers Python     ")
    print("_____________________________________")
    print(" ")
    print("    .--. .-..---. .-..-.             ")
    print("   : .--': :: .; :: :; :             ")
    print("   `. `. : ::  _.':    :.---. .-. .-.")
    print("    _`, :: :: :   : :: :: .; `: :_; :")
    print("   `.__.':_;:_;   :_;:_;: ._.'`._ . :")
    print("                        : :     .-' ;")
    print("                        :_;     `--' ")
    print(" ")
    print("  This application is developed by:  ")
    print("                      Clirim Furriku ")
    print(" ")
    print("_____________________________________")
    print("                                     ")
    print("_____________________________________")
    print("         Project source link:        ")
    print("https://github.com/clirimfurriku/SIPHpy")
    print("______________________________________")
    print(" ")
    print("______________________________________")
    print(" ")


def get_info():
    global proxy, proxy_ip, port
    print("______________________________________")
    print(" ")
    print("  Enter IP address where you want to  ")
    print("                   Start Scanning from")
    print("          Example 192.168.10.1        ")
    print(" ")
    b = input("Enter value a.b.c.d: ")
    print(" ")
    print("______________________________________")
    b = b.split(".")
    a = []
    for element in b:
        a.append(int(element))
    del b
    print(" ")
    print("  Enter IP address where you want to  ")
    print("                     END Scanning     ")
    print("          Example 192.168.100.1       ")
    print(" ")
    b = input("Enter value a.b.c.d: ")
    print(" ")
    print("______________________________________")
    b = b.split(".")
    for element in b:
        a.append(int(element))
    del b
    print(" ")
    print("How many Threads do you want to use:")
    print(" ")
    threads_to_use = int(input("Enter number of threads: "))
    print(" ")
    print("______________________________________")
    print("Do you want to use proxy? ")
    print(" ")
    print("Options")
    print(" ")
    print("0) Do not use proxy")
    print("1) Use proxy")
    print(" ")
    proxy = int(input("Enter Option (0 or 1): "))
    print(" ")
    print("_______________________________________________")
    print(" ")
    proxy_ip = 0
    port = 0
    if proxy == 1:
        proxy_ip = input("Enter Proxy IP:Port (*.*.*.*:****): ")
        print("_______________________________________________")
        print(" ")
        helper = proxy_ip.split(":")
        proxy_ip = helper[0]
        port = int(helper[1])
    return a, threads_to_use


first()
ip, threads = get_info()

start = time()
# #   0, 1, 2, 3,|4, 5, 6, 7

print('Scanning IP Addresses form {}.{}.{}.{} to {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], ip[3],
                                                                     ip[4], ip[5], ip[6], ip[7]))
ip_range = '{}.{}.{}.{} to {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], ip[3],
                                               ip[4], ip[5], ip[6], ip[7])
print("_______________________________________________")
print(" ")
print("Using {} Threads".format(threads))
print("_______________________________________________")
print(" ")
if proxy == 1:
    print("Using Proxy {}:{}".format(proxy_ip, port))
print(" ")

num_of_ip_for_thread, total_num = calculate_thread(ip, threads)

print("_______________________________________________")

while not finished:
    ip = back_calc(ip)

while threading.active_count() > 1:
    print('\rThere are {} threads active'.format(threading.active_count()), end="")
    print('\rScanning \\', end="")
    sleep(0.3)
    print('\rScanning |', end="")
    sleep(0.3)
    print('\rScanning /', end="")
    sleep(0.3)
    print('\rScanning -', end="")
    sleep(0.3)


end = time()
took = end - start
print('\r\nIt took {:.2f}s To Scan {} IP Addresses'.format(took, total_num))
print()
print('Scanned IP Addresses form ' + ip_range)

print("\r_______________________________________________")

# Recommended Threads To run on:
#          Range                  Threads to use           Time To Run      Text output size
#     0.0.0.0 - 0.1.0.0              [450-800]                [170s]              [.MB]
#     0.0.0.0 - 0.5.0.0               [2000]                 [233.47s]           [.MB]
#     0.0.0.0 - 1.0.0.0           [40000-70000]                 []
#     0.0.0.0 - 5.0.0.0           [200000-400000]               []
#     0.0.0.0 - 10.0.0.0          [300000-500000]               []
#     0.0.0.0 - 100.0.0.0        [ NOT TESTED YET]              []
