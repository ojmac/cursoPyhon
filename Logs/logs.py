import logging

""" La libreria logging permite registrar el comportamiento del codigo
Configurar el nivel de registro y el formato del mensaje """

# Configurar el nivel de registro y el formato del mensaje
logging.basicConfig(level=logging.DEBUG, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    filename="logs.log", filemode="a")

# Ejemplo de uso de los diferentes niveles de registro
logging.debug('Este es un mensaje de depuración')
logging.info('Este es un mensaje informativo')
logging.warning('Este es un mensaje de advertencia')
logging.error('Este es un mensaje de error')
logging.critical('Este es un mensaje crítico')

logging.debug('Este es otro mensaje de depuración')





