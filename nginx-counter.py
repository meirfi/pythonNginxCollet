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
        self.topcount = topcount

        self.reafile = readfile
        self.writefile = writefile

    def Log_Analyze(self):
        print "NGINX Log Analyze"

    def summarize(self):
        print "Nginx Log Summarize"

    def write_summary(self):
        """ sorts and writes occurences into file """
        summary = open(self.writefile, 'w')
        summary.write("Log summary\n")
        for key in self.summary:
            list = sorted(self.summary[key].items(), key=lambda x: x[1], reverse=True)
            list = list[:self.topcount]
            summary.write("\nTop "+key+":\n")
            for l in list:
                summary.write(l[0]+": "+str(l[1])+" times\n")
        summary.close()

if __name__ == '__main__':
    nginx_log_file = 'access.log'
    nginx_log_summery_csv = 'nginx_requests_summery.csv'
    # {TIMESTEMP},{GET},{COUNT}
    # {TIMESTEMP},{POST},{COUNT}
    nginx_log_summery_html = 'nginx_requests_summery.html'
    

