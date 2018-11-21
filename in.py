p= float(input("Fut perqindjen vjetore: "))
v=0
k=1

while k<2:
   k += (p/100)*k
   v += 1
   print('Ne vitin e: ', v, ' perqindja eshte: ', k*100)
  

print('Shuma do te dyfishohet per', v, ' vite')