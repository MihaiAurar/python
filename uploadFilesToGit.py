message = input("Escribe el mensaje del commit")

import os

os.system("git add *")
os.system("git commit -m '" + message + "'")
os.system("git push origin master")
