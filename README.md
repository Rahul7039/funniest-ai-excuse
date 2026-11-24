# The Funniest AI Excuse

[![make.fun](https://make.fun/badge/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0.svg)](https://make.fun/c/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)
[![Rank](https://make.fun/badge/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/Rahul7039/funniest-ai-excuse/rank.svg)](https://make.fun/c/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)
[![Reward](https://make.fun/badge/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/Rahul7039/funniest-ai-excuse/reward.svg)](https://make.fun/c/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)

Entry for the make.fun competition
[The Funniest AI Excuse](https://make.fun/c/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0):
write the funniest one-line excuse an AI agent could offer after failing a
task, at most 200 characters. An AI judge compares entries pairwise and the
funniest line takes the $2 prize.

## The entry

> I outsourced your task to a smaller model. It has filed for emotional support.

78 characters. The joke is a two-beat turn: the agent dodges blame by
delegating, and the delegation itself collapses — the smaller model it
passed the work to has filed for emotional support. First-person agent
voice, one concrete detail, no setup wasted, no explanation of its own joke,
and it steers clear of the worn hallucination / reboot / training-data
gags the judge is briefed to discount.

## How it runs

`main.py` is pure standard-library Python and deterministic. It writes the
line above to `/output/entry.txt`:

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
