# wsgi.py
from dotenv import load_dotenv
import os

if os.path.exists('.env'):
    load_dotenv()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyProject.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
