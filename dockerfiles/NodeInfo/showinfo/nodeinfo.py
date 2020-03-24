import requests
import json
import configparser
import os
from NodeInfo.settings import BASE_DIR

config_path = os.path.join(BASE_DIR, 'config.ini')
configer = configparser.ConfigParser()
configer.read('config.ini')
fileConfig = configer['serverinfo']
SERVER_IP = fileConfig['SERVER_IP']
SERVER_PORT = fileConfig['SERVER_PORT']


class Getk8sNodeInfo(object):
    """
    get k8s node info
    """

    def __init__(self):
        self.url = 'http://%s:%s/api/v1/query?' % (eval(SERVER_IP), eval(SERVER_PORT))
        self.nodes = self.get_node('kube_node_info')
        self.ip_route = self.get_ip()

    def get_data(self, metric):
        parameter = {"query": metric}
        datas = json.loads(requests.get(self.url, params=parameter).text)
        return datas

    def get_node(self, metric):
        datas = self.get_data(metric)
        datas = datas['data']['result']
        nodes = []

        for data in datas:
            node = data['metric']['node']
            nodes.append(node)
        return nodes

    def get_cpu(self, metric):
        datas = self.get_data(metric)
        datas = datas['data']['result']
        cpu_route = {}
        for data in datas:
            cpu = data['value'][1]
            node = data['metric']['node']
            cpu_route[node] = cpu
        return cpu_route

    def get_memory(self, metric):
        datas = self.get_data(metric)
        datas = datas['data']['result']
        memory_route = {}
        for data in datas:
            memory = data['value'][1]
            memory = int((int(memory) / 1073741824)) + 1
            node = data['metric']['node']
            memory_route[node] = memory
        return memory_route

    def get_disk(self):
        disk_route = {}
        for node in self.nodes:
            metric = "node_filesystem_size_bytes{kubernetes_io_hostname='%s'}" % node
            datas = self.get_data(metric)
            datas = datas['data']['result']
            disk = ''
            for data in datas:
                disk += data['metric']['mountpoint'] + '&nbsp;' * 6 + str(
                    int((int(data['value'][1]) / 1073741824)) + 1) + 'G' + '<br>'
            disk_route[node] = disk

        return disk_route

    def get_dns_and_role(self):
        dns_route = {}
        role_list = []
        master_list = []
        datas = self.get_data('kubernetes_build_info')
        datas = datas['data']['result']
        for data in datas:
            ip = data['metric']['instance']
            master_list.append(ip.split(':')[0])

        for node in self.nodes:
            ip = self.ip_route[node]
            if ip in master_list:
                role_list.append('master')
            else:
                role_list.append('')
            cmd = 'nslookup %s' % ip
            dns = os.popen(cmd).read().split().pop()
            dns_route[node] = dns
        return dns_route, role_list

    def get_role(self):
        role_list = []
        master_list = []
        datas = self.get_data('kubernetes_build_info')
        datas = datas['data']['result']
        for data in datas:
            ip = data['metric']['instance']
            master_list.append(ip.split(':')[0])

        for node in self.nodes:
            ip = self.ip_route[node]
            if ip in master_list:
                role_list.append('master')
            else:
                role_list.append('')

        return role_list

    def get_ip(self):
        datas = self.get_data('node_ipvs_connections_total{job="kubernetes-service-endpoints"}')
        datas = datas['data']['result']
        ip_list = []
        ip_value = []
        ip_route = {}
        for data in datas:
            ip = data['metric']['instance']
            ip_list.append(ip.split(':')[0])
            ip_value.append(data['value'][1])
        for node in self.nodes:
            metric = 'node_ipvs_connections_total{kubernetes_io_hostname="%s"}' % node
            data = self.get_data(metric)
            data = data['data']['result']
            value_1 = data[0]['value'][1]
            for index, value_2 in enumerate(ip_value):
                if -500 < int(value_1) - int(value_2) < 500:
                    ip_route[node] = ip_list[index]
                    break
        return ip_route

    def get_all_info(self):
        cpu_route = self.get_cpu('kube_node_status_allocatable_cpu_cores')
        memory_route = self.get_memory('kube_node_status_allocatable_memory_bytes')
        disk_route = self.get_disk()
       # role_list = self.get_role()
        dns_route, role_list = self.get_dns_and_role()

        return dns_route, self.ip_route, cpu_route, memory_route, disk_route, self.nodes, role_list


def get_context():
    context = '<!DOCTYPE html>'
    context += '<html lang="en">'
    context += '<head><meta charset="UTF-8"><title>k8s-node-status</title></head>'
    context += '<body><table border="1" bordercolor="#D8D8D8" width="80%" cellspacing="0">'
    context += '<caption><h2>k8s Shanghai Infrastructure</h2></caption>'
    context += '<tr align="center">'
    titles = ['dns','ip', 'cpu', 'memory', 'disk', 'k8s hostname', 'role']
    for item in titles:
        context += '<th height="50">%s</th>' % item
    context += '</tr>'
    nodeinfo = Getk8sNodeInfo()
    dns_route, ip_route, cpu_route, memory_route, disk_route, nodes, role_list = nodeinfo.get_all_info()
    for index, node in enumerate(nodes):
        infos = (
            dns_route[node], ip_route[node], cpu_route[node], memory_route[node], disk_route[node], node,
            role_list[index])
        context += '<tr align="center"><td height="50"><font color="#3572b0">%s</font></td><td height="50">%s</td><td height="50">%s</td><td height="50">%s</td><td height="50">%s</td><td height="50">%s</td><td height="50">%s</td></tr>' % infos
    context += '</table></body></html>'
    return context
