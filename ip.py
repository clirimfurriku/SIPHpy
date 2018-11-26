import time
import sys
import re
import httplib2
import subprocess
import multiprocessing as mp

def first():
   print (" ")
   print (" ")
   print ("            Welcome to IP Header scanner         ")
   print ("_______________________________________________")
   print (" Scanner IP Headers Python")
   print ("_______________________________________________")
   print (" ")
   print (" .--. .-..---. .-..-.             ")
   print (": .--': :: .; :: :; :             ")
   print ("`. `. : ::  _.':    :.---. .-. .-.")
   print (" _`, :: :: :   : :: :: .; `: : ; :")
   print ("`.__.':_;:_;   :_;:_;: ._.'`._ . ;")
   print ("                     : :     .-. :")
   print ("                     :_;     `._.'")
   print (" ")
   print ("This application is developed by Clirim Furriku")
   print (" ")
   print ("               Never change my name            ")
   print ("_______________________________________________")
   print ("       My website is www.bardtech.com.       ")
   print ("_______________________________________________")
   print ("              Project source link.     ")
   print ("    https://github.com/clirimfurriku/SIPHpy ")
   print ("_______________________________________________")
   print (" ")
   print ("_______________________________________________")
   print (" ")
   # Timeout in seconds for checking one host (5-20)
   print (" After finishing see pld.txt.txt in downloads folder")


def hget(ip, rsp, proxy, sprx, port):
   url = "http://%s" %(ip)
   http_interface = ""
   if proxy ==0:
      proxing = httplib2.Http(timeout=1)
   if proxy ==1: 
      proxing = httplib2.Http(proxy_info = httplib2.ProxyInfo(httplib2.socks.PROXY_TYPE_HTTP_NO_TUNNEL, sprx, port), timeout=1)
   http_interface = proxing
   error = 0
   try: 
      response, content = http_interface.request(url, method="HEAD")
      print ("[i] Response status: %d - %s for %s" % (response.status, response.reason, ip))
      rsp.append(ip)
      response.__dict__ 
   except httplib2.ServerNotFoundError, e:
      error +=1
      print (e.message)
   except httplib2.socket.error, msg:
      error +=1
   #   print("\r[-] Error (1) Direct access of IP : %s" % (ip))
   except httplib2.httplib.ResponseNotReady:
      error +=1
     # print("\r[-] Error (2) Direct access of IP: %s" % (ip))
   return rsp




#a.b.c.d = a[0].a[1].a[2].a[3]
#ea.eb...=a[4].b[1]......


def ip_calc(a, times):
   ip= []
   thend = 0
   stops = 0
   print('\n\n[i] Checking from  %d.%d.%d.%d to %d.%d.%d.%d \n' % (a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7]))
   ip.append('%d.%d.%d.%d' % (a[0], a[1], a[2], a[3]))
   while (a[0] <= 255 or a[1] <= 255 or a[2] <= 255 or a[3] <= 255):
      if a[0] == a[4] and a[1] == a[5] and a[2] == a[6] and a[3] == a[7]:
         thend = 1
         #print("\r[+] Successfully calculated IPs")
         break
      a[3] +=1
      if a[3] >= 255:
         a[2] +=1
         a[3] = 0
      if a[2] >= 255:
         a[1] +=1
         a[2] = 0
      if a[1] >= 255:
         a[0] +=1
         a[1] = 0
      if a[0] >= 255:
         break
      times +=1
      ip.append('%d.%d.%d.%d' % (a[0], a[1], a[2], a[3]))
      if stops == 10:
         print("Calculating IPs 100 ended")
         break
      stops += 1
   return a, times, ip, thend

def scaner(ip, proxy, sprx, port):
   rsp = []
   for adress in ip:
      rsp = hget(adress, rsp, proxy, sprx, port)
   results(rsp)

def timecalc(times, timeout):
   ttime = times*timeout
   print (" ")
   if ttime > 60:
      ttime = ttime/60
      print("[i]Total time to finish this scan is: %d minutes" % (ttime))
   else:
      print("[i]Total time to finish this scan is: %d seconds" % (ttime))
   print (" ")


def get_ip():
   print("_______________________________________________")
   print (" ")
   print ("Enter IP adress a.b.c.d-ea.eb.ec.ed")
   print ("Example 192.168.10.1-192.168.10.255")
   print (" ")
   b = raw_input("Enter value (start-end): ")

   print (" ")
   print("_______________________________________________")
   b = re.split("\D", b)
   a = []
   for element in b:
      a.append(int(element))
   print (" ")
   print ("Do you want to use proxy?")
   print (" ")
   print ("Options")
   print (" ")
   print ("0) Do not use proxy")
   print ("1) Use proxy")
   print (" ")
   proxy = int(input("Enter Option (0 or 1): "))
   print (" ")
   print("_______________________________________________")
   print("_______________________________________________")
   print (" ")
   if proxy == 1:
      sprx = raw_input("Enter Proxy IP:Port (*.*.*.*:****): ")
      print("_______________________________________________")
      print("_______________________________________________")
      print (" ")
      helper = re.split("\:", sprx)
      sprx = helper[0]
      port = int(helper[1])
   if proxy ==0:
      sprx = 0 
      port =0
   timeout = 1
   return a, timeout, proxy, sprx, port


def results(rsp):
   for grsp in rsp:
      print '[+] ', grsp, 'is alive'
      subprocess.call('echo %s >> pld.txt' % (grsp), shell=True)

def mthrd(a, start, proxy, sprx, port):
   thend = 0
   times = 1
   t= []
   tnr=1
   whi = 0
   while thend == 0:
      (a, times, ip, thend) = ip_calc(a, times)
      t.append(mp.Process(target=scaner, args=(ip, proxy, sprx, port, )))
   #subprocess.call('echo [i] Thread number To Check IPs is: %d >> pld.txt' % (times), shell=True)
   for threds in t:
      threds.start()
      #print '[+] Started thread', tnr
   #   tnr +=1
      if whi  == 500:
         time.sleep(30)
         whi =0
      whi += 1
      #subprocess.call('echo [i] Thread number %d Started To Check IPs >> pld.txt' % (tnr), shell=True)
   for thred in t:
     # subprocess.call('echo [i] Joining, %s threads are alive>> pld.txt' % (), shell=True)
      if thred.is_alive():
         thred.join(timeout=None)
   return tnr, times

def main():
   (a, timeout, proxy, sprx, port) = get_ip()
   start = time.time()
   (tnr, times) = mthrd(a, start, proxy, sprx, port)
   subprocess.call('echo [i] Checked %d IPs >> pld.txt' % (times), shell=True)
   subprocess.call('echo [i] Threads Used To Check IPs: %d >> pld.txt' % (tnr), shell=True)
   end = time.time() 
   print("")
   took =  end - start
   print'[i] Checked ', times, ' IPs'
   print'[i] Threads Used To Check IPs: ', tnr
   print'[i] Total time to Finish is: ', took
   subprocess.call('echo [i] Time Taken To Check was %s >> pld.txt' % (took), shell=True)


if __name__ == '__main__':
   first()
   #mp.set_start_method('spawn')
   main()