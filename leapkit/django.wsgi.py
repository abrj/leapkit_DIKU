import os
import sys
import site

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('/home/ubuntu/leapkit/lib/python2.7/site-packages')

# Add the app's directory to the PYTHONPATH
sys.path.append('/home/ubuntu/leapkit')
sys.path.append('/home/ubuntu/leapkit/leapkit')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "leapkit.settings")

# Activate your virtual env
activate_env = os.path.expanduser("/home/ubuntu/leapkit/bin/activate_this.py")
execfile(activate_env, dict(__file__=activate_env))

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()