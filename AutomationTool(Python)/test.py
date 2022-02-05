import sys
import subprocess
import json
t = open('test2.json')
data = json.load(t)
lst=[]             ##List to print all 'failed' file

for i in data['Dependencies'][0].keys():
      try:
        str=i+"=="+data['Dependencies'][0][i]
        op=subprocess.check_output(['pip' , 'install' , str])
      except:
        lst.append(i)
        lst.append(data['Dependencies'][0][i])

if lst:
      for i in range(0,len(lst),2):
            print (lst[i],"==",lst[i+1])
else:
      print("Success")
   




