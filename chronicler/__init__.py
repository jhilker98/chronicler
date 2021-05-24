"""Main TUI implementation for chronicler

Author: Jacob Hilker  
Created: 
"""


import py_cui

__version__ = 'v0.0.1'

class ChroniclerApp:

    def __init__(self, master):

        self.master = master
        self.master.add_label('Hello py_cui!!!', 1, 1)


def main():
    root = py_cui.PyCUI(3, 3)
    wrapper =  ChroniclerApp(root)
    root.start()
