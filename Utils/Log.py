import logging

class Log(object):

    #  設定終端機可看到輸出log訊息的最低等級
    #  set_Level: "DEBUG"
    #             "ERROR"
    set_Level = "DEBUG"

    def __init__(self):
        # defined logger object
        self.dev_logger: logging.Logger = logging.getLogger("python")
        # defined log level
        if Log.set_Level == "DEBUG":
            self.dev_logger.setLevel(logging.DEBUG)
        else:
            self.dev_logger.setLevel(logging.ERROR)

        if not self.dev_logger.handlers:
            # defined log handler
            handler: logging.StreamHandler = logging.StreamHandler()
            # defined log formatter
            formatter: logging.Formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            self.dev_logger.addHandler(handler)

    def debug(self, message):
        # defined dubug level log print method
        message = self.dev_logger.debug(message)
        return message

    def info(self, message):
        # defined info level log print method
        message = self.dev_logger.info(message)
        return message

    def warning(self, message):
        # defined warning level log print method
        message = self.dev_logger.warning(message)
        return message

    def error(self, message):
        # defined error level log print method
        message = self.dev_logger.error(message)
        return message

    def critical(self, message):
        # defined critical level log print method
        message = self.dev_logger.critical(message)
        return message