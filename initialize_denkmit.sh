poetry run python manage.py migrate --run-syncdb
poetry run python << END
import os
import django
os.environ["DJANGO_SETTINGS_MODULE"] = 'denkmit.settings'
django.setup()
from django.contrib.contenttypes.models import ContentType
ContentType.objects.all().delete()
END
poetry run python data_loaders/load_models_from_data.py
