from urllib.parse import urlencode 
from urllib.request import Request, urlopen
from datetime import datetime
import json, logging, time, telegram, os, schedule

""" Variables """
today = datetime.today().strftime('%Y%m%d')
token = os.getenv("TOKEN_TELEGRAM")
chat_id = "YOUR_CHATID"

""" Funciones """
def get_vulnerabilities(json, today):
    texto = "REPORTE DE VULNERABILIDADES DEL %s" % datetime.today().strftime('%d-%m-%Y') + '\n'
    for i in range (0, len (json['result'])):
        if(json['result'][i]['advisory']['date'] < today):
            str_titulo = ("TITULO: %s" % json['result'][i]['entry']['title'])
            str_id = ("ID: %s" % json['result'][i]['source']['cve']['id'])
            str_riesgo = ("RIESGO: %s" % json['result'][i]['vulnerability']['risk']['name'])
            texto_string = '\n' + str_titulo + '\n' + str_id + '\n' + str_riesgo + '\n'
            texto = texto + texto_string
    return texto

def get_notification():
    logger.info('Consultando API VulDB')
    if (json['response']['status'] == '200'):
        logger.info('API VulDB Status: %s' % json['response']['status'])
        texto = get_vulnerabilities(json, today)
        return texto
    else:
        logger.warning('API VulDB Status: %s' % json['response']['status'])
        texto = 'Imposible comunicarme con la API'
        return texto

def send_message(token, chat_id, msg):
	bot = telegram.Bot(token=token)
	bot.sendMessage(chat_id=chat_id, text=msg)

""" Llave API para conectarse a VulnDB & Filtro """
post_fields	= { 'apikey': os.getenv("TOKEN_VULDB"), 'advisory_date': today }

""" Request & Conversion del JSON """
request = Request('https://vuldb.com/?api', urlencode(post_fields).encode())
json_data = urlopen(request).read().decode()
json = json.loads(json_data)

""" Logging """
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger('nAutomaticBot')

schedule.every().day.at("14:00").do(send_message, token, chat_id, get_notification())


while True:
    schedule.run_pending()
    time.sleep(30)