from django.db import models

class MailMetadata(models.Model):
    """ to do """
    subject = models.CharField(max_length=255, default='None')
    fron = models.CharField(max_length=255, default='None')
    to = models.CharField(max_length=255, default='None')
    cc = models.CharField(max_length=255, default='None')

class MailActions(models.Model):
    """ to do """
    input = models.TextField()
    cron = models.CharField(max_length=45)
    template_mail = models.TextField()
    last_run = models.DateTimeField('last_run_timestamp')
    is_enabled = models.BooleanField()
    mail_metadata = models.ForeignKey(MailMetadata, on_delete=models.CASCADE)

class MailServer(models.Model):
    """ to do """
    acc_username = models.CharField(max_length=255, default='None')
    acc_password = models.CharField(max_length=255, default='None')
    smtp_address = models.CharField(max_length=255, default='None')
    smtp_port = models.IntegerField()
