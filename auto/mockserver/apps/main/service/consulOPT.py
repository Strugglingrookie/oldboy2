# coding=utf-8
import sys, requests, re
from consul import Consul

reload(sys)
sys.setdefaultencoding('utf-8')


def newAgent(cip, cport):
    return Consul(host=cip, port=cport)


def getAllService(agent):
    newestIndex, services = agent.catalog.services()
    servicesList = services.keys()
    servicesList.remove('consul')
    return servicesList


def getConnectTime(url):
    return requests.head(url).elapsed.total_seconds()


def getService(agent, name):
    newestIndex, nodeList = agent.catalog.service(name)
    if not nodeList:
        raise Exception('There is no service: [%s] can be used!' % name)
    dcset = set()
    for service in nodeList:
        dcset.add(service.get('Datacenter'))
    serviceList = []
    for dc in dcset:
        newestIndex, allNodeList = agent.catalog.service(name, dc=dc)
        for serv in allNodeList:
            serviceId = serv.get('ServiceID')
            healthNodeList = agent.health.checks(name)[1]
            for i in healthNodeList:
                if i.get('ServiceID') != serviceId:
                    continue
                else:
                    health_output = i.get('Output')
                    try:
                        health = re.search(r'HTTP GET (http:.*): 2.*', health_output).group(1)
                    except:
                        health = None
                if health:
                    address = serv.get('ServiceAddress')
                    port = serv.get('ServicePort')
                    serviceList.append({'address': address, 'port': port, 'health': health})
    if len(serviceList) == 0:
        raise Exception('no serveice can be used')
    else:
        ret = ()
        fastest = None
        for s in serviceList:
            health = s.get('health')
            if health:
                http_conn_time = getConnectTime(health)
                if not fastest:
                    fastest = http_conn_time
                    ret = (s['address'], int(s['port']))
                else:
                    if http_conn_time < fastest:
                        ret = (s['address'], int(s['port']))
        return ret


if __name__ == '__main__':
    agent1 = Consul(host='172.29.0.140', port="8500")
    agent2 = Consul(host='172.29.0.15', port="8500")
    agent = Consul(host='172.29.0.15', port="8500")
    print getService(agent2, 'yyfax-agreement-job')
