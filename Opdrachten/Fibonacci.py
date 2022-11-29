# programma voor fibonacci code te laten zien na hoeveel sequences iemand wilt 
fibonacci = int(input("Hoeveel sequences wilt u zien?:"))
# eerste twee sequences
nummer1, nummer2 = 0, 1
begin = 0
#check of de nummer die ingevoerd valid is
if fibonacci <=0:
    print("voer in hoeveel fibonacci code je wilt zien")
#als er 1 fibbonaci is return to nummer1
elif fibonacci == 1:
    print ("Fibonacci code tot ", fibonacci, ":")
    print(nummer1)
#geneer fibonacci code
else:
   print("Fibonacci sequence:")
   while  begin < fibonacci:
       print(nummer1)
       cijfercombo = nummer1 + nummer2
       #rekenwerk voor de correcte fibonacci code
       nummer1 = nummer2
       nummer2 = cijfercombo
       begin += 1
