#coding: utf-8

SOQ = 0
QOS = 0
for i in range(101):
    SOQ = SOQ + i*i
    QOS = QOS + i
print QOS*QOS-SOQ
