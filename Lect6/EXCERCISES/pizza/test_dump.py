import sys
import os
import tabulate

Menu = sys.argv[1]
extension = os.path.splitext(Menu)[1]
if extension == ".csv":
  print(f"CSV!!!!! {Menu} is a CSV!!!")

if extension != ".csv":
  sys.exit("Not a CSV file")

tabulate(All_Items, headers = "firstrow", tablefmt="grid") #makes a table from it all