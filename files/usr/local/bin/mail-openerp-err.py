#!/usr/bin/env python

'''
A simple tool that gets a message as first argument and send it by mail
'''
# Configuration

SMTP_SSL=%(smtp_ssl)s
SMTP_HOST='%(smtp_host)s'
SMTP_PORT=%(smtp_port)d
SMTP_USER='%(smtp_user)s'
SMTP_PASSWORD='%(smtp_password)s'

MAIL_FROM='OpenERP Server'
MAIL_TO= ['%(mail_to)s']

# Code

import sys
import logging

if len(sys.argv)<2:
    logging.error("No message to send")
    sys.exit(-1)

LOG_MESSAGE = sys.argv[1]

import smtplib

if SMTP_SSL:
    conn = smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT)
else:
    conn = smtplib.SMTP(SMTP_HOST, SMTP_PORT)

if SMTP_USER and SMTP_PASSWORD:
    conn.login(SMTP_USER, SMTP_PASSWORD)

MAIL_CONTENT='''Subject: [OPENERP] Server Error
From: %%s
To: %%s

%%s 
''' %% (MAIL_FROM, ", ".join(MAIL_TO), LOG_MESSAGE)

conn.sendmail(SMTP_USER,MAIL_TO,MAIL_CONTENT)
conn.quit()
