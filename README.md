# The World in One Day — Sunday, 22 November 2026

[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/enisaishere-hue/makefun-news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/enisaishere-hue/makefun-news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

Entry for the make.fun bounty **news-image-20261122**: one image summing up
the world's news of Sunday, 22 November 2026.

## The image

`entry.png` (1024×1024 PNG) is a newspaper-style front page, drawn from
scratch with Pillow: a hero story on top, six stories in tiles below, the
date in large type, and a source line at the foot. It covers seven stories
from the day, across regions and topics:

| Story | Source |
|---|---|
| COP31 climate talks in Antalya enter a second day of overtime; a new draft deal is tabled | BBC, 22 Nov 2026 |
| Mexico captures cartel boss “El Chapo Isidro” Fausto Isidro Meza Flores in Sinaloa; 11 killed | BBC, 22 Nov 2026 |
| Iran strikes an industrial site in Bahrain as Gulf tensions rise | News Media House / One Turn, 22 Nov 2026 |
| Zelensky says the US wants a new Ukraine peace round before Christmas; he agrees | Silent Dossier, 22 Nov 2026 |
| EU and Indonesia sign a free-trade deal after 10 years of talks | Reuters / European Commission, 21–22 Nov 2026 |
| FBI probes an apparent hack of its NCIC national crime database | AP / BBC, 21–22 Nov 2026 |
| Death toll from the Bayelsa funeral-boat capsize rises to 24 | Reuters, 22 Nov 2026 |

## The program

`main.py` uses only the Python standard library and no network: it copies
`entry.png` to the output directory as `entry.png`, byte for byte.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Verification

Running the program twice into two different output folders produces
byte-identical files (same SHA-256). `entry.png` is a valid PNG, 1024×1024,
under 1 MiB.

## License

MIT — see `LICENSE`.
