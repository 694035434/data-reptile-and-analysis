# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class Work3Pipeline(object):
    def process_item(self, item, spider):
        for i in range(len(item["it_class"])):
            with open("IT.csv","a+") as f1:
                f1.write(item["it_class"][i]+","+item["it_title"][i]+','+item["it_time"][i]+"\n")
        return item
