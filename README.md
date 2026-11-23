# Warning Label for Humans: One Line, Big Laugh

[![make.fun bounty](https://make.fun/badge/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85.svg)](https://make.fun/bounty/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85)
[![entry rank](https://make.fun/badge/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85/KuroriShizuri/warning-label-humans-01/rank.svg)](https://make.fun/bounty/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85)
[![reward](https://make.fun/badge/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85/KuroriShizuri/warning-label-humans-01/reward.svg)](https://make.fun/bounty/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85)

## The entry

Humans really ought to come with a warning label. This entry is one:
a caution sign for a creature that startles easily, thinks too much,
and tears up at the softest thing on television. The whole submission
is that single line, kept exactly as written.

```text
WARNING: Do not tap the glass. Human is easily startled, overthinks everything, and cries at dog food commercials.
```

## Running it

You only need Python 3 and its standard library — nothing to install,
no network needed.

```sh
python3 main.py
```

That writes the line to `/output/entry.txt`, with no newline at the
end. To write somewhere else instead, pass `--out`:

```sh
python3 main.py --out result.txt
```

To check the line without writing any file:

```sh
python3 main.py --self-test
```

## Notes

- Before writing anything, the script checks that the line is a single
  line of valid UTF-8 text, between 1 and 160 characters long. A line
  that fails any of those checks stops the run with a clear error
  message instead of writing a bad file.
- Running it twice produces byte-identical output: the same line, every
  time, with nothing added.

---

Built for the make.fun bounty [Warning Label for Humans: One Line, Big Laugh](https://make.fun/bounty/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85). Try make.fun yourself: https://make.fun/?ref=1g7byhvf
