from datetime import datetime
from Cheetah.Template import Template
from action_mail_sender import send_mail
import pycron
import requests

resp_action_mail = requests.get('http://127.0.0.1:8000/api/mail/actions/').json()

for objects in range(len(resp_action_mail)):

    if resp_action_mail[objects]['is_enabled']:

        q_input = resp_action_mail[objects]['input']
        cron = resp_action_mail[objects]['cron']
        template_mail = resp_action_mail[objects]['template_mail']
        last_run = resp_action_mail[objects]['last_run']

        last_run = datetime.strptime(last_run, '%Y-%m-%dT%H:%M:%SZ')

        if pycron.is_now(cron, last_run):
            resp = requests.get(f'http://127.0.0.1:8000/api/elastic?query={q_input}').json()
            if bool(resp):
                HTML_BODY = str(Template(template_mail, {'response': resp}))
                #print(HTML_BODY)
                send_mail(HTML_BODY)
            else:
                print("NOT RUN, dict empty")
        else:
            print("NOT RUN, cron not true")
    else:
        print("Alert not enabled!")
        break
