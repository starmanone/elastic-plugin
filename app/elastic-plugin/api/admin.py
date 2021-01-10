from django.contrib import admin

from .models import MailActions, MailMetadata, MailServer

apiModels = [MailActions, MailMetadata, MailServer]
admin.site.register(apiModels)