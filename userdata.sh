#!/bin/bash
yum -y update
yum install epel-release -y
yum install ruby -y
yum install python35 -y
yum install python35-pip -y
yum install -y docker
service docker start
cd /home/ec2-user
