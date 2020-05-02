import ctypes
import os
import time

EnumWindows = ctypes.windll.user32.EnumWindows
EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int),     ctypes.POINTER(ctypes.c_int))
GetWindowText = ctypes.windll.user32.GetWindowTextW
GetWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW
IsWindowVisible = ctypes.windll.user32.IsWindowVisible

#Blacklisted Apps (ones that keep showing up)
blacklist = ['','Backup and Sync', 'ASUSMiniBar', 'Microsoft Text Input Application', 'Microsoft Store', 'Calculator','Program Manager', 'Settings']
currentDir = os.path.realpath(__file__)
apps = []

# https://stackoverflow.com/questions/19336211/finding-opened-applications source

def foreach_window(hwnd, lParam):

    titles = []

    if IsWindowVisible(hwnd):
        length = GetWindowTextLength(hwnd)
        buff = ctypes.create_unicode_buffer(length + 1)
        GetWindowText(hwnd, buff, length + 1)
        titles.append(buff.value)
        if (buff.value not in blacklist):
            apps.append(buff.value)
        #print(buff.value)

    return titles

def getList(category):
    ncurrentDir = currentDir.replace('main.py','')
    relative_path = 'phrases\\'+category+'.txt'
    filePath = ncurrentDir + relative_path
    print(filePath)
    with open(filePath) as f:
        lines = f.read().splitlines()
    return lines


def main():
    youTubeFlag = False
    videoName = ''
    categoryName = 'Unknown Category'
    coding = getList('coding')
    wastingtime = getList('wastingtime')
    sports = getList('sports')
    comedy = getList('comedy')

    EnumWindows(EnumWindowsProc(foreach_window), 0)

    while True:

        print('***Running Applications***')
        for app in apps:
            if 'YouTube' in app:
                youTubeFlag = True
                videoName = app.split('-')[0]
            print('\t'+app)

        if(youTubeFlag):
            print("\n\n\n***Found YouTube Video***")
            for name in coding:
                if(name in videoName):
                    categoryName = 'coding'

            for name in wastingtime:
                if (name in videoName):
                    categoryName = 'wastingtime'
            
            for name in sports:
                if (name in videoName):
                    categoryName = 'sports'

            print(videoName + ' - '+ categoryName)
        else:
            print("\n\n\nNot Watching ForeGround")
        
        time.sleep(30)

   #end of main
if __name__ == "__main__":
    main()




