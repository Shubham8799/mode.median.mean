print("1.mode")
print("2.median") 
print("3.mean") 
operation = input("choose number:")
if operation =="1":
   print("start")
   l = input("put the value of l:")
   f1= input("put the value of f1:")
   f2= input("put the value of f2:")
   f0 = input("put the value of f0 :")
   h = input("put the value of h : ")
   print("f1 - f0")
   f = int(f1) - int(f0)
   print(f)
   f21 = int(2)* int(f1) - int(f0) - int(f2)
   print("2f1 - f0 - f2")
   print(f21)
   print("F1- f0 × h")
   ff2 = int(f) * int(h)
   print(ff2)
   import decimal
   m1=decimal.Decimal(ff2)/ decimal.Decimal(f21)
   print(m1)
   ff3 = decimal.Decimal(m1)+ decimal.Decimal(l)
   print("so,the last step : additional of l by the solving equation")
   print(ff3) 
   print("programe finished")
elif operation =="2":
   #median
   print("median")
   l3= input("put the value of L :")
   cf3= input("put the value of cf:")
   f3= input("put the value of f:")
   h3= input("put the value of h :")
   n3= input("put the value of n:")
   n2 = int(n3)/ int(2)
   print("n/2")
   print(n2)
   ncf = int(n2)- int(cf3)
   print("n/2 - cf")
   print(ncf)
   print("n/2 - cf × h")
   ncf2 = int(ncf) * int(h3)
   print(ncf2)
   print("h× n/2 - cf ÷ f")
   import decimal
   h2= decimal.Decimal(ncf2)/ decimal.Decimal(f3)
   print(h2)
   print("so,our last step")
   print("l + whole equation")
   l2 = decimal.Decimal(h2) + decimal.Decimal(l3)
   print(l2)
   print("done")
elif operation == "3":
   #mean
   print("mean")
   print("formula of mean: fixi / fi")
   fixi = input("put the value of fixi : ")
   fi = input("put the value of fi:")
   import decimal
   answer = decimal.Decimal(fixi) /decimal.Decimal(fi)
   print(answer)
else:
  print(" Invalid input🤨 ") 

   
