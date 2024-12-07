import os

# class is Blueprint or template
class utils:

    def show_disk_space(self): # (self) any object use this function
        print(os.system("df -h")) # for linux (for Windows -> in Txt file)

    # def show_memory(self):
    #     print(os.system("free -m"))
    
    def show_cpu(self):
        print(os.system("lscpu"))

    def show_system_info(self):
        print(os.uname().system)


PC_1 = utils() # object to reuse the Blueprint
PC_1.show_disk_space() # calling the method of class

PC_2 = utils()
PC_2.show_cpu()
