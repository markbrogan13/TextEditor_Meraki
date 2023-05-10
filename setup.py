"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['Editor.py']
DATA_FILES = ['--iconfile']
OPTIONS = {'iconfile': '/Users/mbrogan/Desktop/VSCode/TextEditor_Meraki/assets/editor.icns'}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
