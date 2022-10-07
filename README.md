
## Description

Simple badge generator. Generated badge contains solved problem counters for chosen [Leetcode](https://leetcode.com) user.

Badge example:
![Badge example](https://github.com/nedmv/leetcode-badge/blob/github-actions/badge.png)

## Usage
### Local installation
1. Install dependencies:
`pip install -r requirements.txt`
2. Launch script:
`python3 main.py [--config CONFIG] [--output OUTPUT] LEETCODE_USERNAME`

Default configuration path: `config.yml`

Default output path: `badge.png`

### Github Actions
1. Fork repository and enable Github Actions.
2. Add secret `LEETCODE_USERNAME`. Badge will be generated for this user.
3. Use action `generate-badge`.
It could be launched:
    - manually
    - daily at 00:00 UTC
    - on commits in `main`
4. Access generated badge on branch `github-actions`.