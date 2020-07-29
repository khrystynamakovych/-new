import inspect
import logging

def customLogger(logLevel=logging.DEBUG):
    #Gets the name of the class/method from where this method is called
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
    # By default log all the messages
    logger.setLevel(logging.DEBUG)

    fileHandler = logging.FileHandler("automation.log".format(loggerName), mode='w')
    fileHandler.setLevel(logLevel)

    formatter = logging.Formatter('%(asctime)s: %(name)s: %(levelname)s: %(message)s')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)




    return logger

''' to use it, this module has to be imported
inside a class a variable should be created e. g.
log = custom_logger.customLogger(logging.DEBUG)
to the methods where it will be user logging messages should be added
like: 'self.log.error('error message')'''