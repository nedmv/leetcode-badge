from config import BadgeConfig
from leetcode import LeetcodeUserdata
from generator import generate_badge
import argparse
import yaml

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate badge with given Leetcode user stats.')
    parser.add_argument('user', nargs=1, metavar = 'USER', 
                        help = 'Leetcode username')
    parser.add_argument('--config', nargs=1, metavar = 'PATH', 
                        default = ['config.yml'], 
                        help = 'path to config file (defaults to config.yml)')
    parser.add_argument('--output', nargs = 1, metavar = 'OUTPUT', 
                        default = ['generated/badge.png'], 
                        help = 'path to output file (defaults to generated/badge.png)')
    args = parser.parse_args()

    with open(args.config[0], 'r') as file:
        cfg = yaml.safe_load(file)
    username = args.user[0]
    savepath = args.output[0]
    data = LeetcodeUserdata(username)
    generate_badge(cfg, data, savepath)