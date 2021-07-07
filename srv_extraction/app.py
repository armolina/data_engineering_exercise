from os import listdir
from os.path import isfile, join

files = [f for f in listdir("/tmp") if isfile(join("/tmp", f))]
print(files)