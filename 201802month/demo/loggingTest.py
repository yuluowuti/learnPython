#!/user/bin/env python
# -*- coding:utf-8 -*-
import logging

# logging.basicConfig函数各参数：
#
# filename：指定日志文件名；
#
# filemode：和file函数意义相同，指定日志文件的打开模式，'w'或者'a'；
#
# format：指定输出的格式和内容，format可以输出很多有用的信息，
#
# 参数：作用
#
# %(levelno)s：打印日志级别的数值
# %(levelname)s：打印日志级别的名称
# %(pathname)s：打印当前执行程序的路径，其实就是sys.argv[0]
# %(filename)s：打印当前执行程序名
# %(funcName)s：打印日志的当前函数
# %(lineno)d：打印日志的当前行号
# %(asctime)s：打印日志的时间
# %(thread)d：打印线程ID
# %(threadName)s：打印线程名称
# %(process)d：打印进程ID
# %(message)s：打印日志信息
# datefmt：指定时间格式，同time.strftime()；
# level：设置日志级别，默认为logging.WARNNING；
# stream：指定将日志的输出流，可以指定输出到sys.stderr，sys.stdout或者文件，默认输出到sys.stderr，当stream和filename同时指定时，stream被忽略；

def logtest1():
    # 配置logging基本的设置，然后在控制台输出日志，
    logging.basicConfig(level = logging.DEBUG,
                        format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)

    logger.info("Start print log")
    logger.debug("debug info ")
    logger.warning("warning info ")
    logger.error("error info ")

def logtest2():
    # 将日志写入到文件
    logger = logging.getLogger(__name__)
    logger.setLevel(level=logging.DEBUG)
    handler = logging.FileHandler("log.txt")
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    console = logging.StreamHandler()
    logger.addHandler(console)

    logger.info("Start print log")
    logger.debug("debug info ")
    logger.warning("warning info ")
    logger.error("error info ")

if __name__ == '__main__':
    logtest2()

