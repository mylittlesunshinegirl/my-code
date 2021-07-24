# -*- coding:utf-8 -*-

import logging,os,time


class GetLog:

    def getTime(self):
        """get he current sysdate"""
        self.now=time.strftime("%Y-%m-%d %H-%M-%S")
        return self.now

    def getlog(self, loginfo):  # loginfo
        '''loginfo'''
        # logging.INFO,logging.WARNING
        # logging printing log，logging.basicConfig()function republish the basic setting up of printing log
        time = self.getTime()
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s %(levelname)s -----> %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S',
                            filename = os.path.dirname(os.path.dirname(__file__))+'/Output/logs/%s.txt' % (time),filemode='w')
        logging.info(loginfo)


if __name__=='__main__':

    loger = GetLog()
    loger.getTime()
    print(loger.getTime())
    # loger.report()

