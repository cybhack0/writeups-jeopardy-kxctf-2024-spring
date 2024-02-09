from config.config import Config
from models.command_status import Status
from models.messages import MSG
from models.secret import Secret
from database.database import Database

from aiogram import Bot, Dispatcher, executor, types
import logging, time, datetime

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

cfg = Config()

db = Database(cfg.db)

bot = Bot(cfg.tg.token)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message):
    if not db.is_user_exists(message.chat.id):
        db.add_telegram_user(message.chat.id)
        logger.info(f"Added user {str(message.chat.id)}")
    else:
        db.update_status(message.chat.id, Status.NOTHING)
        
    await bot.send_message(message.chat.id, MSG.HELLO)

@dp.message_handler(commands=["add"])
async def add(message):
    if not db.is_user_exists(message.chat.id):
        db.add_telegram_user(message.chat.id)
        logger.info(f"Added user {str(message.chat.id)}")
    
    db.update_status(message.chat.id, Status.CREATING)
    await bot.send_message(message.chat.id, MSG.ADD)


@dp.message_handler(commands=["get"])
async def get(message):
    if not db.is_user_exists(message.chat.id):
        db.add_telegram_user(message.chat.id)
        logger.info(f"Added user {str(message.chat.id)}")

    db.update_status(message.chat.id, Status.READING)
    await bot.send_message(message.chat.id, MSG.GET)

@dp.message_handler(commands=["list"])
async def list(message):
    if not db.is_user_exists(message.chat.id):
        db.add_telegram_user(message.chat.id)
        logger.info(f"Added user {str(message.chat.id)}")
    
    db.update_status(message.chat.id, Status.NOTHING)

    secrets = db.get_secrets()

    msg = "All secrets:"
    for secret in secrets:
        msg += "\n" + secret[0] + ":" + secret[1].strftime('%c')

    await bot.send_message(message.chat.id, msg)

@dp.message_handler(content_types=['text'])
async def text(message):
    if not db.is_user_exists(message.chat.id):
        db.add_telegram_user(message.chat.id)
        logger.info(f"Added user {str(message.chat.id)}")

    st = db.get_user_status(message.chat.id)

    if st == Status.NOTHING:
        await bot.send_message(message.chat.id, MSG.HELP)

    elif st == Status.CREATING:
        args = message.text.split(":")

        if len(args) != 2 or len(args[0]) == 0 or len(args[1]) == 0: 
            await bot.send_message(message.chat.id, MSG.ERROR_ADD)

        stamp = int(time.time())

        secret = Secret(args[0], message.chat.id, stamp, args[1])
        secret.set_logger(logger)
        db.create_secret(secret.name_secret, datetime.datetime.fromtimestamp(stamp).strftime('%c'), secret.secret, secret.get_passwd(),)
        secret.log_created()

        msg = f'''
            Your secret: 
            {secret.name_secret}:{secret.get_passwd()}    
        '''

        await bot.send_message(message.chat.id, msg)

    elif st == Status.READING:
        args = message.text.split(":")

        if len(args) != 2 or len(args[0]) == 0 or len(args[1]) == 0: 
            await bot.send_message(message.chat.id, MSG.ERROR_GET)

        elif not db.is_secret_exists(args[0], args[1]):
            await bot.send_message(message.chat.id, MSG.ERROR_GET)

        else:
            secret = db.get_secret(args[0],args[1])

            msg = f'''
                Вот твой секрет<З:
                {secret}
            '''
            await bot.send_message(message.chat.id, msg)
    db.update_status(message.chat.id, Status.NOTHING)


executor.start_polling(dp, skip_updates = False)