import sys
arg = int(sys.argv[1])

if arg > 1:
  for index in range(2, arg//2):
    if (arg % index) == 0:
      print(arg, "is not a prime integer")
      break
  else:
    print(arg, "is a prime integer")
else:
  print(arg, "is not a prime integer")