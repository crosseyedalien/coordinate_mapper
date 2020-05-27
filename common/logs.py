import logging

FORMAT = '[[[ %(levelname)s ]]]:[ %(asctime)-9s ]:%(message)s'
logging.basicConfig(format=FORMAT, level=logging.DEBUG, datefmt="%m/%d/%Y %I:%M:%S %p")

