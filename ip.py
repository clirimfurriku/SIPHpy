import os

# Created by Clirim Furriku on 25.03.2018
# Latest update 16.11.2018
# keep it Open Sources

# If you share never change my name 
print (" ")
print (" ")
print ("            Welcome to IP Header scanner         ")
print ("_______________________________________________")
print (" Scanner IP Headers Python")
print ("_______________________________________________")


print (" .--. .-..---. .-..-.            ")
print (": .--': :: .; :: :; :            ")
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
print ("Keep in mind : ")
print (" ")
print ("To make it faster change timeout")
print ("For 3G is recommended 10 sounds time")
print ("For 4G is recommended 3 - 8 seconds")
print ("For timeout lower than required it may contain errors")
print ("_______________________________________________")
print ("_______________________________________________")
# Timeout in seconds for checking one host (5-20)
print("Timeout in seconds for checking one host (3 - 20)")
timeout = 10
print (" ")
timeout = int(input("Enter timeout: "))
print (" ")
print (" After finishing see payload.txt in downloads folder")
print("_______________________________________________")
print (" ")
print ("start IP adress a.b.c.d (ex 192.168.10.1)")
print (" ")
a = int(input("Enter value of a (1 - 255): "))
print (" ")
b = int(input("Enter value of b (1 - 255): "))
print (" ")
c = int(input("Enter value of c (1 - 255): "))
print (" ")
d = int(input("Enter value of d (1 - 255): "))
print (" ")
print("_______________________________________________")
print (" ")
print (" Enter end IP address ea.eb.ec.ed (ex 192.168.10.100)")
print (" ")
#this will check from start IP to end ip
ea = int(input("Enter value of ea (1 - 255): "))
print (" ")
eb = int(input("Enter value of eb (1 - 255): "))
print (" ")
ec = int(input("Enter value of ec (1 - 255): "))
print (" ")
ed = int(input("Enter value of ed (1 - 255): "))
print (" ")

print("_______________________________________________")
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

#If you are not a developer don't need to read more









#IP format in string
ip = '%d.%d.%d.%d' % (a, b, c, d)

#End IP in string
eip = '%d.%d.%d.%d' % (ea, eb, ec, ed)

print("_______________________________________________")


if proxy ==1:
   print ("Using Proxy: %s" % (sprx))


print("_______________________________________________")

print ("Chechking IP's from %s to %s" % (ip, eip))


ttime = 0
cka = a
ckb = b
ckc = c
ckd = d
while (cka < 255 and ckb < 255 and ckc < 255):

  if cka == ea and ckb == eb and ckc == ec and ckd == ed: 
      break
  if ckd == 255:
      ckc +=1
      ckd = 0
  if ckc == 255:
      ckb +=1
      ckc = 0
  if b == 255:
      cka +=1
      ckb = 0
  ckd +=1
  ttime +=timeout
   
ttime = ttime / 60
print (" ")

print("Total time to finish this scan is: %d minutes" % (ttime))
print("_______________________________________________")

print (" ")
os.system('echo ______________________________ >> payload.txt')
os.system('echo This application is created by >> payload.txt')
os.system('echo _________Clirim_Furriku________ >> payload.txt')
os.system('echo ________________________________ >> payload.txt')
os.system('echo _______ Check my website ______ >> payload.txt')
os.system('echo _______ www.bardtech.com _______ >> payload.txt')
os.system('echo ________________________________ >> payload.txt')

os.system('echo Checking IP between %s to %s >> payload.txt' % (ip, eip))

print('Starting to check')
print('Please check payload.txt after finishing')
while (a < 255 and b < 255 and c < 255):
   os.system('echo ___________________________________ >> payload.txt')
   if a == ea and b == eb and c == ec and d == ed: 
      break
   if d == 255:
      c +=1
      d = 0
   if c == 255:
      b +=1
      c = 0
   if b == 255:
      a +=1
      b = 0
   d +=1
   ip = '%s %d.%d.%d.%d' % (ip, a, b, c, d)

if proxy == 0:
  cmd = 'curl --retry 0 -m %d  -I %s -vs >>payload.txt 2>&1' % (timeout, ip)
if proxy == 1:
   cmd = 'curl --retry 0 -m %d -I %s -X %s -vs >>payload.txt 2>&1' % (timeout, ip, sprx)

os.system(cmd)
print("_______________________________________________")
print("_______________________________________________")
print(" ")
print ("Successful")
print ("Please check payload.txt file for output")
print(" ")
print("_______________________________________________")
print("_______________________________________________")
exit
