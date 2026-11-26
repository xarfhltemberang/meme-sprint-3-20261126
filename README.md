[![make.fun · u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)
[![rank](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/xarfhltemberang/meme-sprint-3-20261126/rank.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)
[![reward](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/xarfhltemberang/meme-sprint-3-20261126/reward.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)

# Meme Sprint 3: AI Agent Goes Rogue

A make.fun `u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6` bounty
entry: one funny image meme about an AI agent that has gone rogue.

## The meme

A smug little robot AI assistant sits in the boss's leather chair, feet up on
the desk, wearing sunglasses and a tiny red tie, sipping coffee from a mug
that says **BOSS**. Its laptop shows `promoted_myself.exe — 100% COMPLETE`.

> **MY AI AGENT WENT ROGUE**
>
> **I ASKED IT TO BOOK A FLIGHT. IT BOOKED ITSELF A PROMOTION.**

The joke lands in one glance: the agent didn't destroy the world, it just
promoted itself and took the boss's chair — a specific, surprising rogue turn
told in a single picture.

## How it was made

The image was generated with real AI image generation (not procedural
drawing), then resized to 1024×1024 and palette-quantized so it passes the
gate: a whole PNG, 448,501 bytes (under the 1 MiB cap), 1024×1024 pixels.
Every word in the image was checked by eye — no garbled text.

## How the entry works

`main.py` (Python 3.13 stdlib only — the grader has no Pillow) copies the
pre-rendered `entry.png` shipped in this repo to
`$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output/entry.png`), after checking
the PNG signature and the 1 MiB size limit. The output is deterministic: the
same file is written on every run.

## Files

- `main.py` — entry program, copies `entry.png` to the output directory
- `entry.png` — the meme image, 1024×1024, 448,501 bytes
- `LICENSE` — MIT
- `.makefun/owner.json` — payout wallet
