web: newrelic-admin run-program gunicorn --pythonpath="$PWD/scriptum-backend" wsgi:application
worker: python scriptum-backend/manage.py rqworker default