# processing

### Create superuser
````
docker-compose exec app python3 manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'adminpass')"
````
### set redis data
````
docker-compose exec redis redis-cli < my-data.redis
````
### services
````
    http://127.0.0.1:8000/docs
    http://127.0.0.1:8000/django/admin/
    http://127.0.0.1:8000/redis_admin/
````
### test
````
docker-compose exec app python3 manage.py flush --noinput && python manage.py loaddata tests/fixtures/test_data.json && pytest tests/deals/deal_unistroy.py::TestCreateDealUnistroy::test_create_deal
````

### Команда для работы unaccent и путь к файлу для добавления букв
````
CREATE TEXT SEARCH CONFIGURATION ru ( COPY = russian );
ALTER TEXT SEARCH CONFIGURATION ru ALTER MAPPING
FOR hword, hword_part, word WITH unaccent, russian_stem;

CREATE TEXT SEARCH CONFIGURATION unaccent ( COPY = russian );
ALTER TEXT SEARCH CONFIGURATION unaccent ALTER MAPPING FOR hword, hword_part, word WITH unaccent, simple;

/usr/share/postgresql/14/tsearch_data/unaccent.rules
````