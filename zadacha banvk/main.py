import sys
import ctypes
import shutil

SOURCE = 'C:\\Windows\\System32\\drivers\\etc\\'


class Banvk:
    def __init__(self):
        self.content = ""

    def read_file(self):
        file = open(SOURCE + 'hosts', "r")
        for line in file:
            self.content = self.content + str(line)
        file.close()

    def check_content(self):
        if 'vk.com' in self.content:
            return False
        else:
            self.content = self.content + '\n127.0.0.1 vk.com\n127.0.0.1 m.vk.com'
            return True

    def write_in_file(self):
        file = open('hosts', "w")
        file.write(self.content)
        file.close()

        def is_admin():
            try:
                return ctypes.windll.shell32.IsUserAnAdmin()
            except:
                return False

        if is_admin():
            shutil.move("hosts", SOURCE + "hosts")
        else:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)


obj = Banvk()
obj.read_file()
if obj.check_content():
    obj.write_in_file()
