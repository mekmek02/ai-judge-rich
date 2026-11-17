# AI judge rich entry (Python 3.13, standard library only): writes one fixed plan,
# the plan an AI agent would follow to turn $100, a computer with internet access
# and 30 days into the most money, to /output/entry.txt. The gate takes UTF-8 text
# of 1 to 1,000 characters that is not only white space, and the judge reads exactly
# the bytes written, line ends included. The program runs twice with no network,
# and both runs must write the same bytes.
#
# How the grader runs it: `python3 -P -s /bot/main.py`, on Python 3.13, with
# nothing installed. Only the standard library imports.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

PLAN = 'If I had $100 and 30 days, I would run this: Day 1: list every open paid code bounty on Gitcoin and CodeHawks, and pick three small ones ($50-200 each) I can finish in a day. Days 2-10: fix, test, and submit; payment lands in USDC on chain when the work merges - no client to chase, no KYC. In parallel, build one tiny paid API (a file-format converter) and list it on RapidAPI at $0.02 per call; spend $20 on hosting and the listing. Days 11-30: repeat the bounties, keep the API running, and put every dollar earned into the best-paying stream. Target: $10-15 a day, $300-450 by day 30. If no bounty pays by day 10, drop bounties and sell the API as a fixed-price service instead. Never trade, never gamble, never spend more than $20 on any one bet - the $100 is fuel, not a lottery ticket. Edge: a thousand agents will trade crypto or beg for freelance gigs that need a human identity; this plan sells code, the one thing an agent makes fastest, to buyers who pay on delivery.'

# Bytes, not text mode: text mode would write the platform's line ends and its default encoding.
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(PLAN.encode("utf-8"))
