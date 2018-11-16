import os

# Created by Clirim Furriku on 25.03.2018
# keep it Open Sources

# If you share never change my name 
# Because
# I'm losing my time with this 
print ("               Welcome to PAYLOADER            ")
print ("_______________________________________________")
print (" This application is developed by Clirim Furriku")
print (" ")
print ("               Never change my name            ")
print ("_______________________________________________")
print ("         My website is www.bardtech.com.       ")
print ("_______________________________________________")
print ("I'm waiting my time to create this so respect my work")
print ("Keep in mind : ")
print ("Time for 3G is ")
print ("To check *.*.*.0 to *.*.*.255 Will finish for 1 hour")
print ("To check *.*.0.0 to *.*.255.255 will finish in 12 days")
print ("_______________________________________________")
print ("Time for 4G is")
print ("To check *.*.*.0 to *.*.*.255 Will finish for 35 min")
print ("To check *.*.0.0 to *.*.255.255 will finish in 5.2 Days")
print (" ")
print ("Maybe it doesn't worth it but is faster than usual way")
# For more faster processing i have no time 
print (" ")
print ("To make it faster change timeout")
print ("For 3G is required 15 sounds time")
print ("For 4G is required 7 - 10 seconds")
print ("Actually while testing I used 3-5 sec")
print ("For timeout lower than required it may contain errors")
print ("_______________________________________________")

# Timeout in seconds for checking one host (5-20)
print("Timeout in seconds for checking one host (5 - 20)")
timeout = 10
timeout = int(input("Enter timeout. for one IP: "))

print (" After finishing see payload.txt in downloads folder")
print("_______________________________________________")
print ("start IP adress a.b.c.d (ex 192.168.10.1)")
a = int(input("Enter value of a (1 - 255): "))
b = int(input("Enter value of b (1 - 255): "))
c = int(input("Enter value of c (1 - 255): "))
d = int(input("Enter value of d (1 - 255): "))
print("_______________________________________________")

print (" Enter end IP address ea.eb.ec.ed (ex 192.168.10.100)")
#this will check from start IP to end ip
ea = int(input("Enter value of ea (1 - 255): "))
eb = int(input("Enter value of eb (1 - 255): "))
ec = int(input("Enter value of ec (1 - 255): "))
ed = int(input("Enter value of ed (1 - 255): "))


#If you are not a developer don't need to read more









#IP format in string
ip = '%d.%d.%d.%d' % (a, b, c, d)

#End IP in string
eip = '%d.%d.%d.%d' % (ea, eb, ec, ed)

print ("Do you want to use proxy?")
print ("Options")
print ("0) do not use proxy")
print ("1) use proxy")
proxy = int(input("Enter Option (0 or 1): "))

if proxy == 1:
   sprx = input("Enter Proxy IP:Port (*.*.*.*:****): ")


print ("Chechking IP's from %s to %s" % (ip, eip))


os.system('echo ______________________________ >> payload.txt')
os.system('echo This application is created by >> payload.txt')
os.system('echo _________Clirim_Furriku________ >> payload.txt')
os.system('echo ________________________________ >> payload.txt')
os.system('echo _______ Check my website ______ >> payload.txt')
os.system('echo _______ www.bardtech.com _______ >> payload.txt')
os.system('echo ________________________________ >> payload.txt')

os.system('echo Checking IP between %s to %s >> payload.txt' % (ip, eip))

print('Starting to check')
while (a < 255 and b < 255 and c < 255):
   os.system('echo ___________________________________ >> payload.txt')
   os.system('echo Scanning %s >> payload.txt' % (ip)) 
   if proxy == 0:
     cmd = 'curl -m %d -I http://%s >> payload.txt' % (timeout, ip)
   if proxy == 1:
      cmd = 'curl -m %d -I http://%s -X %s >> payload.txt' % (timeout, ip, sprx)
   os.system(cmd)
   if a == ea and b == eb and c == ec and d == ed: 
      exit()
   if d == 255:
      c += 1
      d = 0
   if c == 255:
      b += 1
      c = 0
   if b == 255:
      a += 1
      b = 0
   print(ip)
   d += 1
   ip = '%d.%d.%d.%d' % (a, b, c, d)

print(ip)
exit
