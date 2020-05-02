import wmi
import win32gui
import win32process

c = wmi.WMI()
# print('hello')
# windowHandle = win32gui.GetForegroundWindow()
# name = win32gui.GetWindowText(windowHandle)

# print(name)

for process in c.Win32_Process():
    print(process.ProcessId, process.Name)