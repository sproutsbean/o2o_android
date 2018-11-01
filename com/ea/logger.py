import logging.config
from com.ea.resource import globalparameter as gl


logging.config.fileConfig(gl.logger_conf)
logger  = logging.getLogger("example01")