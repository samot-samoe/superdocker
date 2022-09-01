#!/bin/bash
pip install sqlalchemy
pip install python-dotenv
superset db upgrade
superset init
superset fab create-admin --username admin --firstname admin --lastname admin --email admin --password admin
# superset load_examples
# SCRIPTPATH="$( cd "$(/app/superset_home/ "$0")" ; pwd -P )"
# superset import-datasources --path /app/externals.yml --sync columns,metrics
superset run -h 0.0.0.0 -p 8088 
# python pip install beautifulsoup4
# SCRIPTPATH="$( cd "$(/app/superset_home/ "$0")" ; pwd -P )"
python /app/superset_home/superset_config.py
