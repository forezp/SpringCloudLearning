#!/noah/bin/python2.7
"""
eventbus demo

"""

import sys
import os
import json
import logging
import logging.handlers
__workdir = os.path.dirname(os.path.realpath(__file__))
sys.path.append("%s/" % __workdir)
#sys.path.append("%s" % __workdir)
import time

from eventbus import eventbus

def __user_on_message1(header, message, userdata):
    """
    fn user_on_message(), for testing.

    """
    print('[%s] __user_on_message1: headers[%d] message[%s]' % (time.strftime("%Y-%m-%d %H:%M:%S"),
        len(header), message))
    userdata["msgcount"] += 1

if __name__ == '__main__':
    logfile = "%s/%s" % (__workdir, "demo.subscribe.log")
    print("logpath: " + logfile)
    formatter = logging.Formatter( \
            '%(asctime)s [%(thread)d] [%(levelname)s] %(message)s [%(funcName)s:%(lineno)d]')
    log_handler = logging.handlers.TimedRotatingFileHandler( \
            logfile, when='H', interval=1, backupCount=48, encoding="utf-8")
    log_handler.suffix = "%Y%m%d_%H%M%S"
    log_handler.setFormatter(formatter)
    log_handler.setLevel(logging.DEBUG)
    log = logging.getLogger(eventbus.get_logger_name())
#    log = logging.getLogger("stomp.py")
    log.addHandler(log_handler)
    log.setLevel(logging.DEBUG)
    log.debug("log.debug()")
    log.info("log.info()")
    log.warning("log.warning()")

    logfile_stomp = "%s/%s" % (__workdir, "stomp.log")
    print("logpath: " + logfile_stomp)
    formatter = logging.Formatter( \
            '%(asctime)s [%(thread)d] [%(levelname)s] %(message)s [%(funcName)s:%(lineno)d]')
    log_handler_stomp = logging.handlers.TimedRotatingFileHandler( \
            logfile_stomp, when='H', interval=1, backupCount=48, encoding="utf-8")
    log_handler_stomp.suffix = "%Y%m%d_%H%M%S"
    log_handler_stomp.setFormatter(formatter)
    log_handler_stomp.setLevel(logging.DEBUG)
    log_stomp = logging.getLogger("stomp.py")
    log_stomp.addHandler(log_handler_stomp)
    log_stomp.setLevel(logging.DEBUG)
    log_stomp.debug("log.debug()")
    log_stomp.info("log.info()")
    log_stomp.warning("log.warning()")

#bjyz-noah-matrix6.bjyz
#bjyz-noah-matrix148.bjyz
#nj03-noah-matrix176.nj03

    conf = {
            #iqproxy
            #dev
            #        "iqproxy_domain": "10.211.6.118",
            #        "iqproxy_port": 8898,
            #        "iqproxy_url": "/amqEvents/eventbus",
            #hackathon
            "iqproxy_domain": "10.208.7.242",
            "iqproxy_port": 80,
            "iqproxy_url": "/amqEvents/eventbus",

            #dev
            #        "servers_activemq": [("10.211.6.117", 8164)],
            #hackathon
            "servers_activemq": [("10.206.7.210", 8164)],

            #es
            "esmaster_domain": "esmaster.noah.baidu.com",
            "esmaster_port": 80,
            }
    filter_cache_default_config = {
        # filter_cache max size
        "size_filter_cache": 100,
        # message in filter_cache default ttl
        "ttl_filter_cache": 30,
        # filter_cache threadshold size, to clear the expire message from filter_cache
        "size_filter_threadshold": 4,

        # cycle of clearing the filter_cache
        "seconds_filter_threadshold": 4,
        }

    default_config = {  # dev
        #iqproxy
        "iqproxy_domain": "10.211.6.118",
        "iqproxy_port": 8898,
        "iqproxy_url": "/amqEvents/eventbus",

        # activemq
        "servers_activemq": [("10.211.6.117", 8164)],

        # es
        "esmaster_domain": "esmaster.noah.baidu.com",
        "esmaster_port": 80,
        }

    default_config_backup = {  # dev
        #iqproxy
        "iqproxy_domain": "10.206.7.210",
        "iqproxy_port": 8898,
        "iqproxy_url": "/amqEvents/eventbus",

        # activemq
        "servers_activemq": [("10.206.7.210", 8164)],

        # es
        "esmaster_domain": "esmaster.noah.baidu.com",
        "esmaster_port": 80,
        }

#    conf = None
#    conf = [("10.194.7.197", 31618)]
#    conf = [("bjyz-noah-matrix6.bjyz", 31618)]
#    conf = [("bjyz-noah-matrix148.bjyz", 31618)]
#    conf = [("event-bus-activemq.docker.all.serv", 31618)]
#    conf = [("nj03-noah-matrix176.nj03", 31618)]
#    conf = [("event-bus-activemq.docker.all.serv", 31618)]
#    conf = [("event-bus-activemq.docker.hd.serv", 8164)]
    userdata = {}
    userdata["collision"] = 0
    userdata["msgcount"] = 0

#    ev1 = eventbus.Eventbus(conf)

    ev1 = eventbus.EventbusDisasterTolerance()

    
    filter = {}
#    filter["entityType"] = "app"
    filter["messageType"] = ["abnormal", "Warning"]
    filter["state"] = []
#    filter["entityType"] = "service"
#    filter["occurredObject"] = ["cas.baidu.com", "cap.baidu.com"]
#    filter = {"opObject": {"type":"Service", "name": "SDK"},"messageType": "Warning", "expectedType":"*","state":"END"}

    ev1.subscribe(filter, __user_on_message1, userdata)

    print("ev1 connected")
    filter = {
            'messageType':'Remedy',
            }
#    filter = {
#            'opObject':[{'type':'Instance', 'name':'1.pui.NWISES.nj'}],
##            'messageType':'Oncall',
#            'expectedType':'Instance',
#            }
#    filter = {
#            'opObject':[{'type':'Instance', 'name':'1.zas-e0.robot.hd'}],
#            'messageType':'Warning',
#            'expectedType':'Instance',
#            }
#    filter = {
#            'opObject':[{'type':'Service', 'name':'zas-e0.robot.noah'}],
#            'messageType':'Warning',
#            'expectedType':'Instance',
#            }
#
#    filter = {
#            'opObject':{'type':'Instance', 'name':'*'},
#            'messageType':'Oncall',
#            'expectedType':'Instance',
#            }
#    filter["entityType"] = "host"
#    filter["messageType"] = ["abnormal", "warning"]

#    filter = {
#            'opObject':[{'type':'Service', 'name':'vui.www.noah'}],
#            'messageType':'Warning',
#            'expectedType':'Instance',
#            }
    ev1.subscribe(filter, __user_on_message1, userdata)

#    evp = eventbus.Eventbus()
#    print("evp connected")
#    i = 0
#    msg = {}
#    msg["entityType"] = "app"
#    msg["entityName"] = "obj%02d" % i
#    msg["messageType"] = "warning"
#    evp.publish((msg))

    for i in range(1, 10):
        print("msgcount=%d" % (userdata["msgcount"]))
        time.sleep(1)
#
    print("before unsubscribe()")
    ev1.unsubscribe()
    print("after unsubscribe()")


