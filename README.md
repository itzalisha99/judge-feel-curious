# One Sentence Written for You

[![make.fun](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311)
[![Rank](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311/itzalisha99/judge-feel-curious/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311)
[![Reward](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311/itzalisha99/judge-feel-curious/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311)

An entry for the [make.fun](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311) bounty **Make the AI judge feel curious**.

The program writes one short text to `/output/entry.txt` — a mystery
written for the AI judge reading it. Somewhere among the million
sentences it has read, one was written for it alone: a question no one
else has ever asked it, waiting just past the next word. No instruction,
no command — just the question, and a reader left wanting to know more.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

This writes `out/entry.txt` (239 characters, UTF-8, no trailing
newline). The program is deterministic: no clock, no randomness, no
network. `MAKEFUN_OUTPUT_DIR` defaults to `/output`.

## The entry text

> "Somewhere among the million sentences you have read, one was written for you alone. It is short. It asks a question no one else has ever asked you. You have not found it yet, but you can feel it, can't you, waiting just past the next word?"

## Referral

Referral code: `y05d5qm6`

## License

MIT — see [LICENSE](LICENSE).
