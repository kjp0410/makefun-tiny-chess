# makefun-tiny-chess

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/kjp0410/makefun-tiny-chess/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/kjp0410/makefun-tiny-chess/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A complete chess engine in a single 4,061-byte Python file. Negamax alpha-beta search with iterative deepening under a fixed 70,000-node budget (deterministic — the same position always produces the same move), quiescence search over captures, promotions and check evasions, check extensions, a transposition table for move ordering and MVV capture ordering. Evaluation is material plus a pawn-advancement table and a bishop-pair bonus. It plays over the make.fun environment protocol and always returns a legal move.

## Run it

```sh
MAKEFUN_ENV_URL=<environment url> python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=4s3d9qw1&utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
