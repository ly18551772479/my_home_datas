#! /bin/sh
export http_proxy="http://child-prc.intel.com:913"
export https_proxy="http://child-prc.intel.com:913"
/usr/bin/python3.5 /root/NodeInfo/manage.py runserver 0.0.0.0:8002

