import sys
import os

Menu = sys.argv[1]
extension = os.path.splitext(Menu)[1]
if extension == ".csv":
  print(f"CSV!!!!! {Menu} is a CSV!!!")

if extension != ".csv":
  sys.exit("Not a CSV file")