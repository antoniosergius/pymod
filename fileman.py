#!/usr/bin/env python3.4

import os.path
import pathlib
import pwd
import stat

def run():
   user = pwd.getpwuid(os.getuid()) 
   #home = str(pathlib.Path(user.pw_dir))
   home = "/home/serginho/Documentos"   
   listdir = os.listdir(home)
   for item in listdir:
      if item.startswith("."):
         print(item)
         continue
      else:
         item = os.path.join(home, item)
         if pathlib.Path(item).is_dir():
            # chmod            
            for (dirpath, dirname, files) in os.walk(item):
               for f in files:
                  path = os.path.join(dirpath, f)
                  # chmod
                  print(path)
         else:
            print(item)
   #print(count)


if __name__ == "__main__":
   run()

























def runold():
   # os.getcwd() retorna a string do diretório corrente
   # e logo em seguida é criado o objeto Path curdir.
   curdir = pathlib.Path(os.getcwd())

   # Retorna um objeto com os campos do /etc/passwd do usuário corrente
   user = pwd.getpwuid(os.getuid()) 
   home = pathlib.Path(user.pw_dir)
   shome= str(home)   
   dirlist = os.listdir(shome)
   for child in home.iterdir():
      wd = home/child
      if wd.is_dir():
         print(wd)
         for grandson in wd.iterdir():
            print(grandson)
#   for child in dirlist:
#      wd = home/pathlib.Path(child)

#      if path.is_dir() and child.startswith("."):
         #print(child+"\n" if child.startswith(".") else "", end="")
 #        print(child)  
