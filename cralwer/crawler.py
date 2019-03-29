# -*- coding: utf-8 -*-
'''
Created on 2019. 3. 29.

@author: jason96
'''

import requests


def clean_url(content):
    pure_urls = []
    for line in content.split('\n'):
        if line.startswith('#'):
            continue
        if line.startswith('//'):
            continue
        line = line.replace('127.0.0.1', '')
        line = line.replace('PRIMARY ', '')
        line = line.replace(' blockeddomain.hosts', '')
        line = line.strip()
        if len(line) > 0:
            pure_urls.append(line)
    return pure_urls


def crawl(url):

    res = requests.get(url)
    return clean_url(res.content)


def load_urls():
    urls = []
    with open('crawler_url.txt') as f:
        for line in f.readlines():
            line = line.replace('\n', '')
            urls.append(line)
    return urls


def crawl_threat_intel():
    crawl_urls = load_urls()
    threat_intels = []
    for url in crawl_urls:
        for x in crawl(url):
            threat_intels.append(x)
    threat_intels = list(set(threat_intels))
    threat_intels.sort()

    with open('crawler_threat_intel_domain.txt', 'w') as f:
        for x in threat_intels:
            f.write(x+'\n')


if __name__ == '__main__':
    crawl_threat_intel()
