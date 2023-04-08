import os
import datetime
import sys

Ny = None

#取目录

Directory = os.getcwd()

# Dos模式

print ("xiaozhao45 Command")
print ("开源项目")
print ("输入exit退出;输入about查看更新内容")
Command1 = input("CMD:" + Directory + " >")
Circulate = 0
while Circulate == 0:
    if Command1 == "":
        print("输入的命令不能为空！")
        Command1 = input("CMD:" + Directory + " >")
    elif Command1 == "exit":
        sys.exit()
    elif Command1 == "cd":
        print("暂不支持此命令！")
        Command1 = input("CMD:" + Directory + " >")
    elif Command1 == "about":
        print("\033[31m更新内容：\033[m")
        print("    1.加入了PowerShell模式，但不支持自定义命令，你可以输入psm来打开")
        print("    2.输入time可以查看当前时间")
        print("当前版本：v1.0")
        print("Github:")
        Command1 = input("CMD:" + Directory + " >")
    elif Command1 == "time":
        today = datetime.date.today()
        print("日期：", today)
        current_time = datetime.datetime.now().time()
        print("时间: ", current_time)
        Command1 = input("CMD:" + Directory + " >")
    elif Command1 == "powershell mode":
        import psm
    elif Command1 == "PSM":
        import psm
    elif Command1 == "psm":
        import psm
    elif Command1 == "help":
        # os.system("help")
        print("""
        ASSOC          显示或修改文件扩展名关联。
    ATTRIB         显示或更改文件属性。
    BREAK          设置或清除扩展式 CTRL+C 检查。
    BCDEDIT        设置启动数据库中的属性以控制启动加载。
    CACLS          显示或修改文件的访问控制列表(ACL)。
    CALL           从另一个批处理程序调用这一个。
    CD             显示当前目录的名称或将其更改。
    CHCP           显示或设置活动代码页数。
    CHDIR          显示当前目录的名称或将其更改。
    CHKDSK         检查磁盘并显示状态报告。
    CHKNTFS        显示或修改启动时间磁盘检查。
    CLS            清除屏幕。
    CMD            打开另一个 Windows 命令解释程序窗口。
    COLOR          设置默认控制台前景和背景颜色。
    COMP           比较两个或两套文件的内容。
    COMPACT        显示或更改 NTFS 分区上文件的压缩。
    CONVERT        将 FAT 卷转换成 NTFS。你不能转换
                   当前驱动器。
    COPY           将至少一个文件复制到另一个位置。
    DATE           显示或设置日期。
    DEL            删除至少一个文件。
    DIR            显示一个目录中的文件和子目录。
    DISKPART       显示或配置磁盘分区属性。
    DOSKEY         编辑命令行、撤回 Windows 命令并
                   创建宏。
    DRIVERQUERY    显示当前设备驱动程序状态和属性。
    ECHO           显示消息，或将命令回显打开或关闭。
    ENDLOCAL       结束批文件中环境更改的本地化。
    ERASE          删除一个或多个文件。
    EXIT           退出 CMD.EXE 程序(命令解释程序)。
    FC             比较两个文件或两个文件集并显示
                   它们之间的不同。
    FIND           在一个或多个文件中搜索一个文本字符串。
    FINDSTR        在多个文件中搜索字符串。
    FOR            为一组文件中的每个文件运行一个指定的命令。
    FORMAT         格式化磁盘，以便用于 Windows。
    FSUTIL         显示或配置文件系统属性。
    FTYPE          显示或修改在文件扩展名关联中使用的文件
                   类型。
    GOTO           将 Windows 命令解释程序定向到批处理程序
                   中某个带标签的行。
    GPRESULT       显示计算机或用户的组策略信息。
    GRAFTABL       使 Windows 在图形模式下显示扩展
                   字符集。
    HELP           提供 Windows 命令的帮助信息。
    ICACLS         显示、修改、备份或还原文件和
                   目录的 ACL。
    IF             在批处理程序中执行有条件的处理操作。
    LABEL          创建、更改或删除磁盘的卷标。
    MD             创建一个目录。
    MKDIR          创建一个目录。
    MKLINK         创建符号链接和硬链接
    MODE           配置系统设备。
    MORE           逐屏显示输出。
    MOVE           将一个或多个文件从一个目录移动到另一个
                   目录。
    OPENFILES      显示远程用户为了文件共享而打开的文件。
    PATH           为可执行文件显示或设置搜索路径。
    PAUSE          暂停批处理文件的处理并显示消息。
    POPD           还原通过 PUSHD 保存的当前目录的上一个
                   值。
    PRINT          打印一个文本文件。
    PROMPT         更改 Windows 命令提示。
    PUSHD          保存当前目录，然后对其进行更改。
    RD             删除目录。
    RECOVER        从损坏的或有缺陷的磁盘中恢复可读信息。
    REM            记录批处理文件或 CONFIG.SYS 中的注释(批注)。
    REN            重命名文件。
    RENAME         重命名文件。
    REPLACE        替换文件。
    RMDIR          删除目录。
    ROBOCOPY       复制文件和目录树的高级实用工具
    SET            显示、设置或删除 Windows 环境变量。
    SETLOCAL       开始本地化批处理文件中的环境更改。
    SC             显示或配置服务(后台进程)。
    SCHTASKS       安排在一台计算机上运行命令和程序。
    SHIFT          调整批处理文件中可替换参数的位置。
    SHUTDOWN       允许通过本地或远程方式正确关闭计算机。
    SORT           对输入排序。
    START          启动单独的窗口以运行指定的程序或命令。
    SUBST          将路径与驱动器号关联。
    SYSTEMINFO     显示计算机的特定属性和配置。
    TASKLIST       显示包括服务在内的所有当前运行的任务。
    TASKKILL       中止或停止正在运行的进程或应用程序。
    TIME           显示或设置系统时间。

    TITLE          设置 CMD.EXE 会话的窗口标题。
    TREE           以图形方式显示驱动程序或路径的目录
                   结构。
    TYPE           显示文本文件的内容。
    VER            显示 Windows 的版本。
    VERIFY         告诉 Windows 是否进行验证，以确保文件
                   正确写入磁盘。
    VOL            显示磁盘卷标和序列号。
    XCOPY          复制文件和目录树。
    WMIC           在交互式命令 shell 中显示 WMI 信息。""")
        print("    PSM            进入PowerShell模式")
        print("    about          查看更新内容")
        print("    time           输出当前时间")
        Command1 = input("CMD:" + Directory + " >")
    else:
        os.system(Command1)
        Command1 = input("CMD:" + Directory + " >")