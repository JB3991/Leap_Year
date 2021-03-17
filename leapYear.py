year = int(input("What is the year?"))

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("This is a leap year ")
    else:
      print("This is Not a leap year")
  else: 
    print("This is a Leap Year")
else:
  print("This is NOT a leap year")