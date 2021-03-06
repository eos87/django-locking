import sys
import logging
from django.conf import settings

LOCK_TIMEOUT = getattr(settings, 'LOCK_TIMEOUT', 1800)
LOCKING_LOG_LEVEL = getattr(settings, 'LOCKING_LOG_LEVEL', logging.INFO)
FORMAT = "[locking] [%(levelname)s] %(message)s"

logging.basicConfig(stream=sys.stderr, level=LOCKING_LOG_LEVEL, format=FORMAT)