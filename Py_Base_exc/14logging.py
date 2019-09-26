# log部分，后续将用于测试中的日志打印

import logging

# 创建一个logger
logger=logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)

# 创建一个handler（处理的意思），用于写入日志文件
fh = logging.FileHandler('test.log')

# 再创建一个handler,用于控制台输出
ch=logging.StreamHandler()

# 定义Handler的输出格式
formatter=logging.Formatter('[%(asctime)s][%(filename)s][line: %(lineno)d][%(levelname)s] ## %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# 给logger添加handler
logger.addHandler(fh)
logger.addHandler(ch)

# 记录一条日志

logger.debug('This message should go to the log file')
logger.info('So should this')
logger.warning('And this, too')
logger.error('error return')
logger.critical('bug,bug')

