import yaml

class BadgeConfig():
    defaults = {
        'username_prefix': '',
        'header_text': 'Leetcode',
        'total_text': '',
        'text_color': 'black',
        'background_color': 'white',
        'easy_color': 'green',
        'medium_color': 'orange',
        'hard_color': 'red',
        'text_size': 16,
        'font_family': 'sans-serif'
    }
    def __init__(self, path: str):
        with open('config.yml', 'r') as file:
            config = yaml.safe_load(file)
        if isinstance(config, dict):
            self.data = config
        else:
            raise ValueError(f'Config must be a dictionary')
    def __getitem__(self, key):
        if (self.data[key] is not None):
            return self.data[key]
        if (BadgeConfig.defaults[key] is not None):
            return BadgeConfig.defaults[key]
        raise ValueError(f'Param {key} not found')
    def __setitem__(self, key, value):
        self.data[key] = value
