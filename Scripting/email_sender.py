# -*- coding: utf-8 -*-
"""
@author: A
"""
import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path    # or os.path

html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = 'Universe'
email['to'] = 'saurabhkragarwal@gmail.com'
email['subject'] = 'You are cooooool'
email.set_content(html.substitute({'name': 'Saurabh'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.login('saurabhagarwal1089@gmail.com', 'saurabh90()')
  smtp.send_message(email)
  print('all good boss!')
