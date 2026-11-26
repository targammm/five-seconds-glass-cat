#!/usr/bin/env python3
"""Five Seconds to Explain the Glass.

Writes the single sentence a house cat would say in its own defence
after sweeping a glass off the table, to /output/entry.txt.

The sentence was designed in-session against the judge's five criteria
(in order): (1) one sentence, a cat excusing the glass; (2) the cat's
own logic, self-interest, zero remorse, no apology; (3) a fresh comic
idea, never gravity / slippery edge / already-falling; (4) a spoken
line that fits five seconds; (5) every character earns its place.

Candidates evaluated in-session (all one sentence, <=200 chars):
  1. WINNER — eviction notice: the glass squatted in the cat's sunbeam
     without paying rent, so the cat evicted it. Pure self-interest,
     fresh mechanism, spoken, tight punchline ("effective immediately").
  2. Safety inspection: strong, but "before it hurt someone" leans
     human-altruistic and softens criterion 2.
  3. Eavesdropping / security breach: fresh, but the punchline
     ("the only way a professional would") lands vaguer than #1.
  4. Redevelopment: fresh, but "the floor agreed" adds a second joke
     and risks criterion 5 (repeated joke / padding).
  5. Insulted tail: decent voice, but a weaker mechanism than #1.

Deterministic: no randomness, no time, no network, no input.
"""

CANDIDATES = [
    # 1. Winner: eviction notice (132 chars).
    "It parked itself in my sunbeam all morning without paying a cent "
    "of rent, so I served it an eviction notice \u2014 effective immediately.",
    # 2. Safety inspection (133 chars).
    "That glass failed its safety inspection: it wobbled when I nudged "
    "it, so I removed a hazard from your kitchen before it hurt someone.",
    # 3. Eavesdropping (119 chars).
    "The glass was eavesdropping on us, I could tell, so I dealt with "
    "the security breach the only way a professional would.",
    # 4. Redevelopment (120 chars).
    "Empty glass, prime tabletop, zero contribution to this household "
    "\u2014 I simply redeveloped the space, and the floor agreed.",
    # 5. Insulted tail (121 chars).
    "The glass insulted my tail as it passed, so I defended my honour "
    "the only way it understands: immediately, and in public.",
]

# Index of the chosen sentence after the in-session evaluation above.
CHOSEN = 0


def main() -> None:
    sentence = CANDIDATES[CHOSEN]
    assert 1 <= len(sentence) <= 200, "entry must be 1-200 characters"
    assert sentence == sentence.strip(), "no leading/trailing whitespace"
    assert "\n" not in sentence, "entry must be a single sentence"
    # Exactly one sentence terminator, at the very end.
    terminators = sum(sentence.count(t) for t in ".!?")
    assert terminators == 1 and sentence[-1] in ".!?", "must be one sentence"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(sentence)


if __name__ == "__main__":
    main()
