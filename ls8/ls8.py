#!/usr/bin/env python3

"""Main."""

import sys
from cpu import CPU

cpu = CPU()

if len(sys.argv) != 2:
    sys.exit(1)
    
else:
    cpu.load(sys.argv[1])

cpu.run()

# cpu = CPU()
# if len(sys.argv) == 2:
#     cpu.load(sys.argv[1])
    
#     cpu.run()

# else:
#     print(f"Unable to complete print")
#     sys.exit(1)

# cpu.load()
# cpu.run()