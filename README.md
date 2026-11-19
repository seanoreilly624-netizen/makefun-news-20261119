# 19 November 2026 — The World in One Day

[![make.fun](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/seanoreilly624-netizen/makefun-news-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/seanoreilly624-netizen/makefun-news-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119)

An entry for the make.fun bounty
[Sum up 19 November's world news in one image](https://make.fun/bounty/news-image-20261119).

The image sums up Thursday 19 November 2026 in six stories, drawn as a
one-page newspaper front: a first-ever Trump–Xi–Putin summit in Shenzhen,
Israel's ground push in central Gaza, oil tankers hit by mines near the
Strait of Hormuz, the World Court's Rohingya genocide ruling, the launch of
Grand Theft Auto VI, and Anthropic's Nasdaq debut.

## How it is made

`build_image.py` draws `entry.png` (1024×1024) with Pillow: every icon is
a shape drawn by the script and every word is rendered text — no AI image
generation, no photos, no borrowed artwork. `main.ts` (Node 22, standard
library only) copies `entry.png` to the output directory after checking it
really is a PNG.

```sh
python3 build_image.py
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

## License

MIT — see [LICENSE](LICENSE).
