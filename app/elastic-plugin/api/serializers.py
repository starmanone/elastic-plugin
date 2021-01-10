from rest_framework import serializers
from .models import MailActions, MailMetadata, MailServer

class MailActionsSerialezer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MailActions
        fields = ['id', 'input', 'cron', 'template_mail', 'last_run', 'is_enabled', 'mail_metadata_id']

class MailMetadataSerialezer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MailMetadata
        fields = ['subject', 'fron', 'to', 'cc']

class MailServerSerialezer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MailServer
        fields = ['acc_username', 'acc_password', 'smtp_address', 'smtp_port']
