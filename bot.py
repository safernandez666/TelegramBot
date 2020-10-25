from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters
from engine import get_chiste
import yaml, logging
""" Variable para Manejo de Estados en la Conversacion """
INPUT_TEXT = 0 
def start(update, context):
    logger.info('He recibido un comando start')
    update.message.reply_text('¡Bienvenido al Actualizador de Compromisos %s!' % update.message.from_user.name)
def chiste(update, context):
	update.message.reply_text(get_chiste())
def ioc(update, context):
    update.message.reply_text('Es necesario que me pases el mensaje para parsearlo %s.' % update.message.from_user.name)
    return INPUT_TEXT
def updateIoc(update, context):
    logger.info('Se recibio el Text a Parsear')
    text = update.message.text 
    logger.info('El Texto: %s' % text)
    update.message.reply_text('Se recibio el IoC, procederemos a Parsearlo.')
    ConversationHandler.END

if __name__ == '__main__':

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    logger = logging.getLogger('nAutomaticBot')
    
    """ Cargamos las Configuraciones """
    with open("config.yml", "r") as ymlfile:
        cfg = yaml.load(ymlfile)

    """ Llave API para conectarse a Telegram """
    updater = Updater(token=cfg["telegram"]["token"], use_context=True)

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