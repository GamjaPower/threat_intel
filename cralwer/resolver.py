# -*- coding: utf-8 -*-
'''
Created on 2019. 3. 29.

@author: jason96
'''

import dns.resolver
import time

dns.resolver.timeout = 1
dns.resolver.lifetime = 1


def load_threat_intel_domain():

    domains = []
    with open('crawler_threat_intel_domain.txt') as f:
        for x in f.readlines():
            x = x.replace('\n', '')
            domains.append(x)
    return domains


def resolve_domain():

    dns.resolver.default_resolver = dns.resolver.Resolver(configure=False)
    dns.resolver.default_resolver.nameservers = ['8.8.8.8',
                                                 '168.126.63.1',
                                                 '168.126.63.2',
                                                 '210.220.163.82',
                                                 '219.250.36.130',
                                                 '164.124.107.9',
                                                 '203.248.242.2',
                                                 '8.8.4.4']

    with open('crawler_threat_intel_ip.txt', 'w') as f:
        for threat_intel_domain in load_threat_intel_domain():
            try:
                answers = dns.resolver.query(threat_intel_domain, 'a')
                for answer in answers:
                    print answer.address, threat_intel_domain
                    f.write(answer.address+','+threat_intel_domain+'\n')
            except Exception:
                pass
            finally:
                time.sleep(0.01)


if __name__ == '__main__':
    resolve_domain()
