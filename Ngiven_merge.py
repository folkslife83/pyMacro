import glob
import os

path = os.path.dirname(os.path.realpath(__file__))
os.chdir(path)

path_dir = 'C:\\Git\\pyMacro\\nHgiven'
file_list = os.listdir(path_dir)
date_list = []

for file in file_list:
    if "SIMULATION" not in file:
        date_list.append(file[:10])
date_set = set(date_list)

read_files = glob.glob("C:\\Git\\pyMacro\\nHgiven\\*.txt")

for date in date_set:
    name = "C:\\Git\\pyMacro\\nHgiven\\"+date + ".txt"

    if os.path.exists(name):
        os.remove(name)
    else:
        print("The file does not exist")
    with open(name, "wb") as outfile:
        for f in read_files:
            print(f)
            if f[23:33] == date and "SIMULATION" not in f:        
                with open(f, "rb") as infile:
                    outfile.write(infile.read())
                


for file in file_list:
    #with open(file, "w") as f:
    #    pass

    if len(file) > 14:  #.txt 까지 포함한 파일명 길이
       os.remove("C:\\Git\\pyMacro\\nHgiven\\"+file)

        
                
