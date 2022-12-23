import subprocess
import os

EXEFILE =  "puzzel1.exe"  # Exe File Name

def filesize():
    count = 0
    for root,dir,files in os.walk("puzzels/"):
        count += len(files)
    return count
    
def main():
    FILE = filesize()
    for i in range(13):
        puzzle  = open("puzzels/"+"puzzel"+ str(i+1)+".txt",'r')
        answer = open("answer/"+"answer"+ str(i+1)+".txt",'r')
        
        data = "".join(puzzle.readlines())
        data2= "".join(answer.readlines())
        
        print("Test Case",i+1,"\n\nInput:")
        print(data,"\nOutput:")
        out = subprocess.run([EXEFILE,"-","-"],shell=True,input=data.encode(),capture_output=True)
        print(out.stdout.decode())
        print("\nExpected:")
        print(data2)
        print("\nReturn Code:",out.returncode,"\n")
        print("************************************************","\n")
        
        puzzle.close()
        answer.close()

if __name__ == '__main__':
    main()