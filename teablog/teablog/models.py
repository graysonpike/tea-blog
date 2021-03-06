from django.db import models


class PageView(models.Model):
    viewed_on = models.DateTimeField(auto_now_add=True)
    ip = models.GenericIPAddressField(null=True)
    user_agent = models.CharField(max_length=512, null=True)
    path = models.CharField(max_length=512)
