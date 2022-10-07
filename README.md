
## Description

Simple badge generator. Generated badge contains solved problem counters for chosen [Leetcode](https://leetcode.com) user.

## Usage
1. Install dependencies:
`pip install -r requirements.txt`
2. Launch script:
`python3 main.py [--config CONFIG] [--output OUTPUT] LEETCODE_USERNAME`

Default configuration path: `config.yml`
Default output path: `generated/badge.png`

## Requirements
- Python 3.6+
- [Pillow 8.0+](https://pillow.readthedocs.io/)
- [gql](https://github.com/graphql-python/gql)
- [PyYAML](https://pyyaml.org/)
