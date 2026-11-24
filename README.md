# news-image-20261124

Sum up 24 November 2026's world news in one image.

Entry for https://make.fun/bounty/news-image-20261124
($100 prize pool, 50 places; deadline 2026-11-26 09:00 JST,
Round 2 closes 2026-11-25 09:00 JST).

## What the image shows

- **24 NOVEMBER 2026 — THE WORLD IN ONE DAY**
- NVIDIA brings back Huang — shares jump 31% as Jensen Huang returns as CEO.
- Ukraine sinks Russian warship — naval drones sink the corvette Merkury off Libya.
- Tankers hit in Hormuz — three tankers struck by mines in the Strait of Hormuz.
- Airspace breaches — Russian aircraft enter South Korea's air defence zone;
  a Russian drone briefly enters Polish airspace.
- Indonesia factory fire — 26 killed, dozens missing in Banten.
- Markets rally — S&P 500 up 4.7%, Nikkei up 3.9%.

Sources: public news coverage of 24 November 2026 (Just Security Early
Edition, One Turn News, Naharnet, The Global Eye).

## How it works

`main.py` (Python 3.13, standard library only, no network) copies the bundled
image `asset/entry.png` to `/output/entry.png`. The output is byte-identical
on every run. `render.py` is the readable source the image was made from
(Pillow, render-time only — not used by `main.py`).

- Output: 1024 x 1024 px PNG, 105,794 bytes (limit: 1024 x 1024, 1 MiB).
- Verified: two consecutive runs produce identical SHA-256.

## License

MIT — see LICENSE.
