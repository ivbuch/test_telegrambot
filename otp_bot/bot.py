import sys, traceback, time, logging

from config import Config
from hotp_bot import HOtpBot

config = Config()
logging.basicConfig(filename='example.log', level=logging.INFO)

if __name__ == "__main__":

    bot = HOtpBot(config)
    print("app started")
    while True:
        try:
            logging.debug("do work")
            updates = bot.process()
            time.sleep(config.sleepTimeout)
            logging.info('Waiting {} seconds'.format(config.sleepTimeout))
        except:
            print("Exception in user code:")
            traceback.print_exc(file=sys.stdout)
            raise Exception("Exception in user code")
