import glob
import os

for filename in glob.glob("valid__malware/*.csv"):
    with open(os.path.join(os.getcwd(), filename), 'r') as f:
        file = ''
        while True:
            line = f.readline()
            split_num = line.split(" ")
       # print(split_num[0])
            file += split_num[0] + '\n'
            if line == '': 
                f = open(os.path.join(os.getcwd(), filename), 'w')
                f.write(file)
                f.close()
                break
   
