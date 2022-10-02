from config import BadgeConfig
from leetcode import LeetcodeUserdata
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import argparse

def load_fonts():
    font_dir = 'fonts'
    font_files = fm.findSystemFonts(fontpaths=font_dir)
    for font in font_files:
        fm.fontManager.addfont(font)

def set_font_params(config: BadgeConfig):
    plt.rcParams['font.family'] = config['font_family']
    plt.rcParams['font.size'] = config['text_size']

def num_width(value: int):
    return max(len(str(value)), 1)

def generate_badge(username: str, cfg: BadgeConfig):
    data = LeetcodeUserdata(username)
    fig, ax = plt.subplots()

    left_width = max(len(data.name) + len(cfg['username_prefix']) + 2, len(cfg['header_text']))
    right_width = 15 # (4+1)*3
    width = left_width + right_width
    height = 5

    load_fonts()
    set_font_params(cfg)
    size = plt.rcParams['font.size']
    dpi = ax.figure.dpi
    ax.figure.set_size_inches(width*size/dpi, height*size/dpi)

    easy_pos = left_width/width
    medium_pos = easy_pos+(num_width(data.user_easy) + 1)/width
    hard_pos = medium_pos+(num_width(data.user_medium) + 1)/width
    
    text_color = cfg['text_color']
    ax.text(left_width/2/width, 3/height, cfg['header_text'], color = text_color, ha = 'center')
    ax.text(left_width/2/width, 1/height, f"{cfg['username_prefix']}{data.name}",color = text_color, ha = 'center')
    ax.text(left_width/width, 3/height, f"{cfg['total_text']} {data.user_total:04d}", color = text_color)
    ax.text(easy_pos, 1/height, f'{data.user_easy:04d}', color = cfg['easy_color'])
    ax.text(medium_pos, 1/height, f'{data.user_medium:04d}', color = cfg['medium_color'])
    ax.text(hard_pos, 1/height, f'{data.user_hard:04d}', color = cfg['hard_color'])

    fig.patch.set_facecolor(cfg['background_color'])

    plt.axis('off')
    plt.show()
    fig.savefig("generated/badge.png")
    fig.savefig("generated/badge.svg")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate badge with given Leetcode user stats.')
    parser.add_argument('--user', nargs=1, metavar = 'USERNAME', required = True, help = 'Leetcode username')
    parser.add_argument('--config', nargs=1, metavar = 'PATH', default = ['config.yml'], help = 'path to config file (defaults to config.yml)')
    args = parser.parse_args()

    cfg = BadgeConfig(args.config[0])
    generate_badge(args.user[0], cfg)
    
    


    