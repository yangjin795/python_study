import logging
log_format = '%(threadName)s %(asctime)s %(name)s %(message)s'
logging.basicConfig(filename='example.log',level = logging.DEBUG, format=log_format)
logging.info('I am info')
logging.debug("I am debug")
logging.error('I am error')
