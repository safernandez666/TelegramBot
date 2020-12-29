from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters
from engine import get_chiste, get_ips, get_hash
import yaml, logging, os, time
import schedule

""" Variable Semaforo Estados en la Conversacion """
INPUT_TEXT = 0 

""" Funciones """
def start(update, context):
    logger.info('He recibido un comando start')
    update.message.reply_text('¡Bienvenido al Actualizador de Compromisos %s!' % update.message.from_user.name)
def chiste(update, context):
    logger.info('Consultando API Chiste')
    update.message.reply_text(get_chiste())
def ioc(update, context):
    logger.info('Dialogo IOC')
    update.message.reply_text('Es necesario que me pases el mensaje para parsearlo %s.' % update.message.from_user.name)
    return INPUT_TEXT
def updateIoc(update, context):
    logger.info('Se recibio el Text a Parsear')
    text = update.message.text 
    logger.info('Las Direcciones IP: %s' % get_ips(text))
    update.message.reply_text('Se recibio el IoC, procederemos a aplicar los siguientes cambios.Direcciones IPs %s' % get_ips(text))
    ConversationHandler.END

""" Main del Programa """
if __name__ == '__main__':

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    logger = logging.getLogger('nAutomaticBot')

    """ Llave API para conectarse a Telegram """
    updater = Updater(token=os.getenv("TOKEN_TELEGRAM"), use_context=True)
    dp = updater.dispatcher

    """ Handler's """
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('chiste', chiste))
    dp.add_handler(ConversationHandler(
        entry_points=[
            CommandHandler('ioc', ioc)
        ],
        states={
            INPUT_TEXT: [MessageHandler(Filters.text, updateIoc)]
        },
        fallbacks=[]
    ))

    updater.start_polling()
    updater.idle()