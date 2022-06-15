from django.db import models


class PageView(models.Model):
    viewed_on = models.DateTimeField(auto_now_add=True)
    ip_from_proxy = models.GenericIPAddressField(null=True)
    http_x_forwarded_for = models.CharField(max_length=512, null=True)
    path = models.CharField(max_length=512)
