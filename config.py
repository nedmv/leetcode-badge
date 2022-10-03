import yaml

class BadgeConfig(yaml.YAMLObject):
    yaml_tag = u'!BadgeConfig'
    yaml_loader = yaml.SafeLoader

    #Defaults
    username_prefix = ''
    username_color = 'black'
    header_text = 'Leetcode'
    total_text = 'Solved: '
    total_text_color = 'black'
    total_color = 'blue'
    header_color = 'black'
    background_color = 'white'
    easy_color = 'green'
    medium_color = 'orange'
    hard_color = 'red'
    text_size = 16
    font_family = 'monospace'
    font_path = 'fonts/digital-7.regular.ttf'
