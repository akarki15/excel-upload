import sys
import logging

logging.basicConfig(stream=sys.stderr)

sys.path.insert(0,"/var/www/demere/demere")

from demere import demere as application
