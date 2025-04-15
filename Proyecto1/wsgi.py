"""
WSGI config for PrimeraPagina project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""
# filepath: c:\Users\Paco\Desktop\_\F\CoderHouse\Python\TuPrimeraPagina+MartinezZorzi\TuPrimeraPagina-MartinezZorzi\Proyecto1\wsgi.py
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Proyecto1.settings')  # Asegúrate de que sea 'Proyecto1.settings'

application = get_wsgi_application()
