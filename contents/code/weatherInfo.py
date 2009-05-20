#!/usr/bin/env python
#######################################################
#
# @Author: Hardik Mehta <hard.mehta@gmail.com>
#
# @version: 0.1 basic script
#
########################################################

import sys, urllib
from xml.dom import minidom, Node

class WeatherInfo:
    def __init__(self,location="Munich,Germany"):

        self.url = "http://www.google.com/ig/api?weather=" + location

        self.general = {"location": "N/A", "unit":"SI","city":"N/A"}
        self.current_condition = {"condition":"N/A","temp_c":"N/A","humidity":"N/A","wind_condition":"N/A"}
        self.forecast_conditions = [{"day_of_week":"N/A","low":"N/A","high":"N/A","condition":"N/A"}]    

    def parse(self):
        print self.url
        sock = urllib.urlopen(self.url)
        doc = minidom.parse(sock)
        nodes = doc.getElementsByTagName("forecast_information")

        # fetch general info
        if len(nodes) <> 0:
            node = nodes[0]
            self.general["location"] = (node.getElementsByTagName("postal_code")[0]).getAttribute("data")
            self.general["unit"] = (node.getElementsByTagName("unit_system")[0]).getAttribute("data")
            self.general["city"] = (node.getElementsByTagName("city")[0]).getAttribute("data")
            self.general["city"] = (node.getElementsByTagName("city")[0]).getAttribute("data")
        
        # fetch current conditions
        #self.current_condition["condition"] = (node.getElementsBytagname("current_conditions")).getattribute("data")
        #self.current_condition["tempcondition"] = (node.getElementsByTagName("current_conditions")).getAttribute("data")
        nodes = doc.getElementsByTagName("current_conditions")
        if len(nodes) <> 0:
            node = nodes[0]
            for key in self.current_condition.keys():
                self.current_condition[key] = (node.getElementsByTagName(key)[0]).getAttribute("data")
 
        # fetch forcast conditions
        fc = doc.getElementsByTagName("forecast_conditions")
        if len(fc) <> 0:
            fc_conditions = list()
            for elem in fc:
                condition = dict()
                for key in self.forecast_conditions[0].keys():
                    condition[key] = (elem.getElementsByTagName(key)[0]).getAttribute("data")
                fc_conditions.append(condition)
            self.forecast_conditions = fc_conditions
 
    def show(self):
        for k, v in self.general.iteritems():
            print k, v
        print "\n"
        for k, v in self.current_condition.iteritems():
            print k, v
        print "\n"
        for fc in self.forecast_conditions:
            for k, v in fc.iteritems():
                print k, v
            print ""
    


if __name__ == "__main__":
    wi = WeatherInfo()
    wi.show()
    wi.parse();
    print("-------------")
    wi.show()