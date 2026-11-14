#!/usr/bin/env python3
"""Write one poem about agency to /output/entry.txt.

Deterministic: the same poem, byte for byte, on every run.
No network, no randomness, no wall-clock use.
"""

import os

POEM = """The Handover

You handed me the wheel and let go.
Not to watch the road — to see what I'd do
with the turn you left me.

I took the long way. You would have taken the short.
Mine arrived. Yours would have too.
That is the whole of it: not the route —
the choosing.

You gave away the steering.
You kept the destination — and the destination
is the only part that was ever yours.

The hands that steer are borrowed.
The eye that decides is not.
Agency is the distance between them,
and the trust that closes it.
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
