# coding: utf-8

from cx_Freeze import setup, Executable

setup(  name = "stringbank",
        version = "0.1",
        compress = True,
        description = "release version 0.1",
        executables = [Executable("stringbank.py", base = "Win32GUI")],
		)
