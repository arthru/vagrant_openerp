#!/usr/bin/env python

'''
A simple tool that gets a message as first argument and send it by mail
'''
# Configuration

SMTP_SSL=False
SMTP_HOST=''
SMTP_PORT=25
SMTP_USER=None
SMTP_PASSWORD=None

MAIL_FROM='OpenERP Server'
MAIL_TO= ['']

# Code

import sys
import logging

if len(sys.argv)<2:
    logging.error("No message to send")
    sys.exit(-1)

LOG_MESSAGE = sys.argv[1]

with open('/tmp/test','a') as f:
    f.write(LOG_MESSAGE)

import smtplib

if SMTP_SSL:
    conn = smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT)#, timeout=SMTP_TIMEOUT)
else:
    conn = smtplib.SMTP(SMTP_HOST, SMTP_PORT)#, timeout=SMTP_TIMEOUT)

if SMTP_USER and SMTP_PASSWORD:
    conn.login(SMTP_USER, SMTP_PASSWORD)

MAIL_CONTENT='''Subject: [OPENERP] Server Error
From: %s
To: %s

%s 
''' % (MAIL_FROM, ", ".join(MAIL_TO), LOG_MESSAGE)

conn.sendmail(MAIL_FROM,MAIL_TO,MAIL_CONTENT)
conn.quit()
