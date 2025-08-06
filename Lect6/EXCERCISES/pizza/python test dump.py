import sys
import os

Menu = sys.argv[1]
extension = os.path.splitext(Menu)[1].lower

if extension != "csv":
  sys.exit("Not a CSV file")