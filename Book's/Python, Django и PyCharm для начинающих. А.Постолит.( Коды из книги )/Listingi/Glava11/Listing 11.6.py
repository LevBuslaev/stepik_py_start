# Listing 11.6
# Heroku: Обновление конфигурации базы данных из $DATABASE_URL.
import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
