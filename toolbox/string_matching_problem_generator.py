import argparse
import random

import numpy as np
from loguru import logger

parser = argparse.ArgumentParser()
parser.add_argument("--alphabet", default="abcd")
parser.add_argument("-t", type=int, default=32)
parser.add_argument("-p", type=int, default=5)
parser.add_argument("-n", type=int, default=10)
parser.add_argument("--no-force-matching", default=False)


def _to_str(a): return ''.join(a)


def main(args):
    output = ''
    _alphabet = [a for a in args.alphabet]
    for _ in range(args.n):
        text = np.random.choice(_alphabet, args.t, replace=True)
        pat = np.random.choice(_alphabet, args.p, replace=True)
        if not args.no_force_matching:
            idx = random.randint(0, args.t - args.p + 1)
            text[idx:idx+args.p] = pat
        output += f"\n{_to_str(text)}\n{_to_str(pat)}"
    logger.info(f"Generated Sets: {output}")


if __name__ == '__main__':
    main(parser.parse_args())
