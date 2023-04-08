import subprocess
import os
import datetime

Directory = os.getcwd()

ctrl = 1
Command = input("PSM:" + Directory + " >>>")

while ctrl == 1:
    if Command == "about":
        print("这是PowerShell模式，输入exit退出")
        Command = input("PSM:" + Directory + " >>>")
    elif Command == "exit":
        print("Good Bye!")
        import Dos
    elif Command == "time":
        today = datetime.date.today()
        print("日期：", today)
        current_time = datetime.datetime.now().time()
        print("时间: ", current_time)
        Command = input("PSM:" + Directory + " >>>")
    else:
        result = subprocess.run(["powershell.exe", Command], capture_output=True, text=True)
        print(result.stdout.rstrip())
        Command = input("PSM:" + Directory + " >>>")
