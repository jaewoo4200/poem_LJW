import sys

if float(sys.version[:3]) > 3.6:
    from .LJW_Upgrade import *
else:
    from .LJW_legacy import *
