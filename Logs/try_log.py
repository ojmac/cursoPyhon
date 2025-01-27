import logging

# Configure logging
logging.basicConfig( filemode='w')

try:
    division = 2/0
except:
    logging.error("Division por 0")
    logging.exception("Division por 0")

logger = logging.getLogger(" personalizado")    
print (logger)

logger.warning("Log de advertencia")

