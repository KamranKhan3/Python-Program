import os

os.system("tput setaf 2")
print("\t\t\t\tWelcome To My Menu")
os.system("tput setaf 7")
print("\t\t\t\t------------------"   )
print()
print()
os.system("tput setaf 6")
print("Press 1 : to date")
os.system("tput setaf 1")		 
print("Press 2 : to cal")
os.system("tput setaf 3")
print("Press 3 : to ls")
os.system("tput setaf 4")
print("Press 4 : to mkdir")
os.system("tput setaf 7")

print("Enter Your Choice:",end='')
ch=input()
print(ch)
if   int(ch) == 1:
         os.system("tput setaf 6")
         os.system("date +%r | espeak-ng -s 140")
         os.system("date +%r")
	
elif int(ch) == 2:
         os.system("tput setaf 1")         
         os.system("cal | espeak-ng -s 140")
         os.system("cal")
         
elif int(ch) == 3:
        os.system("tput setaf 3")
        os.system("ls | espeak-ng -s 140")
        os.system("ls")
elif int(ch) == 4:
        os.system("tput setaf 4")
        os.system("mkdir hi | espeak-ng -s 140")
        os.system("mkdir hi")
else:
    print("not supported | espeak-ng -s 140")
    print("not supported")
os.system("tput setaf 7")
print("\t\t\t\t------------------"  )		






