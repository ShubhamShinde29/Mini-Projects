import cx_Freeze
import os 
import sys
base=None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Program Files\Python311\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Program Files\Python311\tcl\tk8.6"

executables = [cx_Freeze.Executable("Get_Registered.py",base=base,icon="appicon.ico")]

cx_Freeze.setup(
    name="Get_Registered",
    options={"build_exe" : {"packages":["tkinter","os","PIL","pymysql"],"include_files" : ["appicon.ico",'tcl86t.dll','tk86t.dll','database','img']}},
    version="1.0",
    description="Student Registartion Portal | Developed by Shubham Shinde",
    executables=executables
)