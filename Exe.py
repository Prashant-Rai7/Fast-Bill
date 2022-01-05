import cx_Freeze
import sys
import os
base = None
if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Python310\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Python310\tcl\tk8.6"

executables = [cx_Freeze.Executable("Bill.py", base=base,icon="Bill Logo.ico")]

cx_Freeze.setup(
    name = "Fast Bill",
    options = {"build_exe": {"packages":["tkinter","os","sys"], "include_files":['tcl86t.dll','tk86t.dll','Bill Logo.ico','bills']}},
    version = "1.0000001",
    description = "Fast Bill is a Billing Software with all Required Features in the Billing in Super Market and Malls | Developed by Prashant Rai ",
    executables = executables
    )