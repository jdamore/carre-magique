import sys

import magic

if len(sys.argv)<2:
	print("Usage: python3 main.py [dimension]")
	sys.exit(1)

magic = magic.Magic(int(sys.argv[1]))
magic.square()
print(magic.to_s())