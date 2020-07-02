import os
import win32api
def data():
    drives = win32api.GetLogicalDriveStrings()
    drives = drives.split('\000')[:-1]
    #for i in range(len(drives)):
            #print(drives[i])
    #val=input('Enter the disk ')
    #for i in os.listdir(val+':\\'):
        #print(i)
    return drives
def get_val(self,master):
        val=str((self.list_box.get(ACTIVE)))

    
