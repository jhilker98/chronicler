"""Main TUI implementation for Chronicler."""


import py_cui as pycui
import argparse
import yaml
import os
_version_ = 'v0.0.1'

class ChroniclerApp:
    """
    Main TUI implementation for Chronicler.

    Attributes:
        __color_map__ (dict{str, py_cui.color}): Used to map a string from the config file to the interface.
    """        
    __color_map__ = {'white': pycui.WHITE_ON_BLACK, 'black': pycui.BLACK_ON_WHITE,'red': pycui.RED_ON_BLACK, 'green': pycui.GREEN_ON_BLACK, 'yellow': pycui.YELLOW_ON_BLACK, 'blue': pycui.BLUE_ON_BLACK, 'purple': pycui.MAGENTA_ON_BLACK, 'cyan': pycui.CYAN_ON_BLACK, 'lightred': pycui.RED_ON_WHITE, 'lightgreen': pycui.GREEN_ON_WHITE, 'lightyellow': pycui.YELLOW_ON_WHITE, 'lightblue': pycui.BLUE_ON_WHITE, 'lightpurple': pycui.MAGENTA_ON_WHITE, 'lightcyan': pycui.CYAN_ON_WHITE
            }

    def __init__(self, screen):
        """
        Used to initialize the application.

        Args:
            screen (py_cui.PyCUI): The screen the app will be rendered on.
        """
        self.screen = screen
        self.character_list = self.screen.add_scroll_menu('Characters', 0, 0, row_span = 8, column_span = 3, pady = -1)
        self.character_war_info = self.screen.add_block_label('', 0, 3, row_span = 8, column_span = 5, pady = -1, center=False)
        self.widgets = {'character_list': self.character_list, 'character_info': self.character_war_info, 'title_bar': self.screen.title_bar, 'status_bar': self.screen.status_bar}
        self.screen.set_status_bar_text(' q: Quit Chronicler |  o: Open AAR | H: Print Keybindings') 

    #def show_help_menu(self):
    #    keys = ['H: Toggle Help Menu', 'q: Quit Chronicler']
    #    self.screen.show_message_popup('Keybindings','H: Toggle Help Menu     q: Quit Chronicler     o: Open AAR     a: Add Item     s: Save AAR')
    
    
    def run(self):
        """
        Used to run Chronicler.

        This function is an alias for running the Chronicler application.
        """
        self.screen.start()

def parse_config(app, config_file=os.path.expanduser("~/.config/chronicler/config.yml")):
    """
    Used to parse the config file.

    This function parses the configuration file and applies any relevant options to the application. 

    Args:
        app (ChroniclerApp): Application to apply changes to.
        config_file (str, optional): The path to the configuration file. Defaults to "~/.config/chronicler/config.yml".
    
    Raises:
        FileNotFoundError: If the file passed does not exist.
    """
    with open(config_file, 'r') as config_file:
        config = yaml.safe_load(config_file)
        keys = config.keys()
       
        
        #print(keys)
        for key in keys:
            try:
                print(key) 
            except:
                pass
        #TODO get config parsing working
            
def main():
    """
    Run at the command line.

    This function is executed when you run `chronicler` at the command line. It sets up the UI, parses the config, and then runs the application.
    """
    root = pycui.PyCUI(8, 8)
    root.set_title('Chronicler for Crusader Kings 3')
    app =  ChroniclerApp(root)
    #root.add_key_command(pycui.keys.KEY_H_UPPER, app.show_help_menu)
    parser = argparse.ArgumentParser(description='A tool for managing after-action reports for Crusader Kings 3.')
    parser.add_argument('-c', '--config', help='Path to another config file.', action='store', dest='cfg', nargs='?', const="~/.config/chronicler/chronicler.yml")
    args = vars(parser.parse_args())
    #print(args)
    if (args['cfg'] == None):
        parse_config(app)
    else:
        parse_config(app, args['cfg'])    
    #app.run()
