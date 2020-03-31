# coding=utf-8
import logging


class Testut():

    logging.basicConfig(level=logging.INFO)       # logging的输出级别默认是warning，如果想输出更低则需要设置level=logging.INFO
    # log = logging.getLogger('hys')
    # log.setLevel(logging.INFO)
    def test_logging(self):
        self.log.warning("这里输出的是logging的warning")
        self.log.info("这里输出logging的info")