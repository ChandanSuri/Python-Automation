def BoxPrint(symbol, width, height):
	if(len(symbol) != 1):
		raise Exception("'Symbol' needs to be of length 1...")
	if(width < 2 or height < 2):
		raise Exception("Width and height should be greater than 2...")

	print(symbol * width)
	for i in range(height-2):
		print(symbol + (' '  (width - 2)) + symbol)
	print(symbol  * width)

BoxPrint('*', 15, 5)
# asserts are used for detecting programmer errors that are not meant to be
# recovered from... User errors should raise Exceptions...

# logging
import logging

# a file name can also be given to log all the messages in a file rather than on console...
logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
# to disable logging
logging.disable(logging.CRITICAL)
# logging.debug()
# logging.info()
# logging.warning()
# logging.error()
# logging. critical()
# In increasing order of logging for error types (according to gravity)

# don't use print messages for debugging...
