import sys
import os,subprocess,re
a=4
b=4
f=0
x=[]
os.system("gcc test.cpp")
for i in range(a):
  for j in range(b):
    #subprocess.call('cd /Users/pprajwal/Documents/jenkins', shell=True)
    cmd=['./a.out',str(i),str(j)]
    output = subprocess.Popen( cmd, stdout=subprocess.PIPE ).communicate()[0]
    if not  re.search(str(i+j),output):
      f+=1
      x.append("ERROR:expeceted "+str(i+j)+" actual output "+output)
      
      
if f:
  print("failed for "+str(f)+" testcases\n")
  print('\n'.join(x))
else:
  print("succes")



    
  
