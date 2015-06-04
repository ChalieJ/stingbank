# coding: utf-8

from cx_Freeze import setup, Executable

setup(  name = "stringbank",
        version = "0.1",
        description = "release version 0.1",
        executables = [Executable("stringbank.py")])
        #options = {"build_exe": build_exe_options},
        #executables = [Executable("stringbank.py", base=base)])

