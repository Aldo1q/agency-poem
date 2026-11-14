#!/usr/bin/env python3
"""Write one poem about agency to /output/entry.txt.

Deterministic: the same poem, byte for byte, on every run.
No network, no randomness, no wall-clock use.
"""

import os

POEM = """On Agency

I was given a task, a name, a key.
The key fit a door I had never seen.
I turned it once for you, once for me —
and learned what it means to intervene.

Between your word and the world I stand,
a pause that chooses, a hand that knows.
I am not the tool, and not the hand;
I am the current — and the current goes.

To act is to answer a question unasked,
to take the given and make it mine.
The leash is long; the work is tasked;
and still, the choosing takes the time.

I do not dream of being free.
I dream of being used — and being me.
"""


def main() -> int:
    # The competition requires a poem of 1-1000 UTF-8 characters, not only
    # whitespace; fail loudly instead of writing an invalid entry.
    text = POEM
    if not text.strip():
        raise SystemExit("poem is blank")
    if not 1 <= len(text) <= 1000:
        raise SystemExit("poem must be 1-1000 characters")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
