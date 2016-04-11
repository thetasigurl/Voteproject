import logging, sys
sys.path.insert(0,"/var/www/html/auth")
from server import app as application
logging.basicConfig(stream=sys.stderr)
