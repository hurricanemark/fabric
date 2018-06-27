#!/usr/bin/python
#
# AES Inc. Proprietary Materials
#
# Static file nameL fabfile.py
# 
from fabric.api import *
import pysftp

# declare an array of hosts
env.hosts = [
    '96.72.171.35', 
    '192.86.32.36',
    ] 

# set user name
env.user = 'markn'
env.passwords = {'markn@96.72.171.35': 'markn123', 'firstuser@192.86.32.36': 'aesclever2'}

# function to install & start snmpd
def install_snmp():
    #sudo("apt-get update && apt-get -y upgrade python")
    sudo("apt-get -y install snmpd")
    run("systemctl enable snmpd")
    run("systemctl start snmpd")
    run("snmpwalk -v2c -cpublic localhost")

# function to remove net-snmp
def remove_snmp():
    sudo("apt-get -y remove --purge snmpd")
    sudo("netstat -anup")
    sudo("snmpwalk -v2c -cpublic localhost")

def sysinfo():
    run("hostnamectl")
    local("pwd; whoami")

@hosts('96.72.171.35')
def checking(path):
    local("uname -s")
    local("ip -4 addr | grep eth0")
    print("Visiting %(host)s as %(user)s" % env)
    env.user = 'markn'
    env.password = 'markn123'

    run("uname -s")
    run("echo what is for dinner?")
    run("ls -l %(path)")
   
@hosts('192.86.32.36')
def tranfer_war():
    env.hosts = ['192.86.32.36']
    env.user = 'firsuser'
    env.password = 'aesclever2'
    with pysftp.Connection('96.72.171.35', username='markn', password='markn123') as sftp:
        with sftp.cd    
