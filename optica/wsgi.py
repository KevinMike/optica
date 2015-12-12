"""
WSGI config for optica project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "optica.settings")

application = get_wsgi_application()

'''
import os
import sys
import site

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('C:/Users/kevin/optica-latyna/Lib/site-packages')
# Add the app's directory to the PYTHONPATH
sys.path.append('c:/xampp/htdocs/optica')
os.environ['DJANGO_SETTINGS_MODULE'] = 'optica.settings'
# Activate your virtual env
activate_env=os.path.expanduser("C:/Users/kevin/optica-latyna/Scripts/activate_this.py")
execfile(activate_env, dict(__file__=activate_env))
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
'''