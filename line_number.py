import sys
if len(sys.argv) == 1:
    file= input("filename: ")
elif len(sys.argv) == 2:
    if sys.argv[1] == '-h':
        print("Esse programa mostra o(s) numero(s) de linha de um arquivo"); sys.exit(0)
    else:
        file = sys.argv[1]
else:
    sys.exit(f"usage: {sys.argv[0]} filename")

def check_file(file):
    import os
    data=os.popen("ls").readlines()
    if file+'\n' not in data:
        sys.exit("error! file not found.") 

def read(file):
    with open(file,"rb") as file:
        
        data = file.readlines()
        n=0
        for i in data:
            n+=1
            print(n,i.decode("ascii"),end='')

check_file(file)

read(file)
