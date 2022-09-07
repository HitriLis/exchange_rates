# processing

### Create superuser
````
docker-compose exec app python3 manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'adminpass')"
````

### services
````
    http://127.0.0.1:8000/docs
    http://127.0.0.1:8000/django/admin/
````
