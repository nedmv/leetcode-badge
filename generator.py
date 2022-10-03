from PIL import Image, ImageFont, ImageDraw
from leetcode import LeetcodeUserdata
from config import BadgeConfig

def generate_badge(cfg: BadgeConfig, data: LeetcodeUserdata, savepath: str):
    size = cfg.text_size
    fnt = ImageFont.truetype(cfg.font_path, size)

    width = {}
    width['header'] = fnt.getlength(f' {cfg.header_text} ');
    width['username'] = fnt.getlength(f' {cfg.username_prefix}{data.name} ')
    width['left'] = int(max(width['header'], width['username']))

    width[' '] = fnt.getlength(' ')
    width['total'] = fnt.getlength(f'{cfg.total_text}{data.user_total:04d}')
    width['easy'] = fnt.getlength(f'{data.user_easy:04d}')
    width['medium'] = fnt.getlength(f'{data.user_medium:04d}')
    width['hard'] = fnt.getlength(f'{data.user_hard:04d}')
    width['counters'] = width['easy'] + width['medium'] + width['hard'] + 3 * width[' ']
    width['right'] = int(max(width['total'], width['counters']))

    badge = Image.new("RGB", (width['left'] + width['right'], 2*size), cfg.background_color)

    draw = ImageDraw.Draw(badge)

    top = size // 2
    bottom = 3*size // 2

    draw.text((width['left']//2, top), cfg.header_text, font = fnt, anchor = 'mm', fill = cfg.header_color)
    draw.text((width['left']//2, bottom), f'{cfg.username_prefix}{data.name}', font = fnt, anchor = 'mm', fill = cfg.username_color)

    draw.text((width['left'] + width['right']//2 - width['total']//2, top), cfg.total_text, font = fnt, anchor = 'lm', fill = cfg.total_text_color)
    draw.text((width['left'] + width['right']//2 + width['total']//2, top), f'{data.user_total:04d}', font = fnt, anchor = 'rm', fill = cfg.total_color)
    draw.text((width['left'] + width['right']//2, bottom), f'{data.user_medium:04d}', font = fnt, anchor = 'mm', fill = cfg.medium_color)
    draw.text((width['left'] + width['right']//2 - width['medium']//2 - width[' '], bottom), f'{data.user_easy:04d}', font = fnt, anchor = 'rm', fill = cfg.easy_color)
    draw.text((width['left'] + width['right']//2 + width['medium']//2 + width[' '], bottom), f'{data.user_hard:04d}', font = fnt, anchor = 'lm', fill = cfg.hard_color)
    badge.save(savepath)
