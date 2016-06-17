import os
import configparser, itertools

APP_ENV = os.environ.get('APP_ENV') or 'dev'
CONFIG_FILE = os.path.join(os.path.dirname(os.path.realpath(__file__)), '{}.ini'.format(APP_ENV))

SECRET_KEY = '1_w^o90&7%maaag94#-_yv+)g8+l0w934d8we@qec3oryo-2b6'

CONFIG = configparser.ConfigParser()
CONFIG.read(CONFIG_FILE)
# with open(CONFIG_FILE) as cfgfile:
#     CONFIG.read_file(itertools.chain(['global'], cfgfile), source=CONFIG_FILE)

POSTGRES = CONFIG['POSTGRES']

DB_CONFIG = (POSTGRES['user'], POSTGRES['password'], POSTGRES['host'], POSTGRES['database'])
DB_URL = 'postgresql+psycopg2://%s:%s@%s/%s' % DB_CONFIG
