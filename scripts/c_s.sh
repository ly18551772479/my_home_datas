#! /bin/bash
qemu-img create -f raw /localdisk1/vir_datas/centos76_sda_kvm$1.img 200G
qemu-img create -f raw /localdisk1/vir_datas/centos76_sdb_kvm$1.img 400G
qemu-img create -f raw /localdisk2/vir_storages/centos76_sdc_kvm$1.img 600G
virt-install -n centos76_s_kvm$1 -r 16384 --vcpus=8 --disk /localdisk1/vir_datas/centos76_sda_kvm$1.img,format=raw,size=200 --network bridge=br0 --os-type=linux --cdrom /root/Images/CentOS-7-x86_64-DVD-1810.iso --graphics vnc,listen=0.0.0.0
