
## Description

Simple badge generator. Generated badge contains solved problem counters for chosen [Leetcode](https://leetcode.com) user.

Badge example:

<picture>
<source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/nedmv/leetcode-badge/github-actions/badge-dark.png">
<source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/nedmv/leetcode-badge/github-actions/badge-light.png">
<img alt="Badge example." src="https://raw.githubusercontent.com/nedmv/leetcode-badge/github-actions/badge.png">
</picture>

## Usage
### Local installation
1. Install dependencies:
`pip install -r requirements.txt`
2. Launch script:
`python3 main.py [--config CONFIG] [--output OUTPUT] LEETCODE_USERNAME`

Default configuration path: `config.yml`

Default output path: `generated/badge.png`

### Github Actions
1. Fork repository and enable Github Actions.
2. Add secret `LEETCODE_USERNAME`. Badge will be generated for this user.
3. Use action `generate-badge`.
It could be launched:
    - manually
    - each Monday at 00:00 UTC
    - on commits in `main`
4. Access generated badge on branch `github-actions`.