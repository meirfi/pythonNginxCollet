#!/usr/bin/env python
import os


    
class Nginx_Log_Analyzer():
    """ Parses and summarized nginx logsfile """

    def __init__(self, readfile, write_csv_file=None, write_html_file=None):
        """ Initializing """

        self.summery_results = {
            "requests": {},
            "ips": {},
            "useragents": {}
        }

    def Log_Analyze(self):
        print "NGINX Log Analyze"

    def summarize(self):
        print "Nginx Log Summarize"


if __name__ == '__main__':
    nginx_log_file = 'access.log'
    nginx_log_summery_csv = 'nginx_requests_summery.csv'
    # {TIMESTEMP},{GET},{COUNT}
    # {TIMESTEMP},{POST},{COUNT}
    nginx_log_summery_html = 'nginx_requests_summery.html'
    

