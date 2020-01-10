gunicorn --workers=4 --worker-class=gthread -b 0.0.0.0:9000 wsgi:app --log-level=debug --log-file=log/logger.log
