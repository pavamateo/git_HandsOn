#!/usr/bin/env python

import sys, re
from argparse import ArgumentParser

# Classify a sequence as DNA or RNA
parser = ArgumentParser(description='Classify a sequence as DNA or RNA')

# Input sequence argument
parser.add_argument("-s", "--seq", type=str, required=True, help="Input sequence")

# Motif argument for motif search
parser.add_argument("-m", "--motif", type=str, required=False, help="Motif")

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()

# Convert sequence to uppercase
args.seq = args.seq.upper()

# Check if the sequence is DNA or RNA
if re.search('^[ACGT]+$', args.seq):
    print('The sequence is DNA')
elif re.search('^[ACGU]+$', args.seq):
    print('The sequence is RNA')
else:
    print('The sequence can be DNA or RNA')

if args.motif:
    # Convert motif to uppercase
    args.motif = args.motif.upper()

    # Perform motif search
    print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end='')
    if re.search(args.motif, args.seq):
        print("Motif found in motif branch!")
    else:
        print("Motif not found")


