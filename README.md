# makefun-tiny-chess

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/kjp0410/makefun-tiny-chess/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/kjp0410/makefun-tiny-chess/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A complete chess engine in a single 3,288-byte Python file (readable source: `engine.py`, packed with the make.fun kit's `compress`). 0x88 board with make/unmake, Zobrist transposition table with exact/lower/upper scores, killer-move ordering, MVV-LVA captures, null-move pruning, quiescence over captures, promotions and check evasions, and full rules: castling, en passant, all four promotions. Evaluation is material plus formula piece-square tables (pawn advance/centre, knight/bishop/queen centralisation, rook on the 7th, king middlegame/endgame interpolation) and a bishop-pair bonus. Negamax alpha-beta with iterative deepening under a fixed 120,000-node budget (deterministic — the same position always produces the same move). It plays over the make.fun environment protocol and always returns a legal move; perft is exact against the reference counts on six test positions.

## Run it

```sh
MAKEFUN_ENV_URL=<environment url> python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=4s3d9qw1&utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
