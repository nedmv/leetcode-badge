from collections import UserDict
import yaml
import warnings
class BadgeConfig(UserDict):
    data = {
        'username_prefix'  : '',
        'header_text'      : 'Leetcode',
        'total_text'       : 'Solved: ', 

        'username_color'   : '#54aeff',  #blue
        'total_text_color' : '#d0d7de',  #white
        'total_color'      : '#54aeff',  #blue
        'header_color'     : '#ffa116',  #orange
        'background_color' : '#22272e',  #dark
        'easy_color'       : '#00b8a3',  #green
        'medium_color'     : '#ffc01e',  #orange
        'hard_color'       : '#ef4743',  #red

        'text_size'        : 24,  #pixels
        'font_path'        : 'fonts/digital-7.regular.ttf',
        'num_format'       : '',
        'hide_username'    : False
    }

    def __init__(self, path = ''):
        try:
            with open(path, 'r') as file:
                cfg = yaml.safe_load(file)
            if isinstance(cfg, dict):
                for key, val in cfg.items():
                    if key in self.data:
                        self.data[key] = val
                    else:
                        warnings.warn(f"Config param '{key}' is not recognized.")
            else:
                warnings.warn(f"Config is not dictionary. Continue with default params.")     
        except IOError:
            warnings.warn(f"Failed to process configuration file '{path}'. Continue with default params.")

    def format(self, value: int):
        return f"{value:{self.data['num_format']}}"
