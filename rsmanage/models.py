from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


# Create your models here.

class Resource(models.Model):
    resource_hostname = models.CharField(max_length=250, blank=False, verbose_name="主机hostname")
    resource_ip = models.GenericIPAddressField(protocol='both', verbose_name="主机ip")
    resource_port = models.SmallIntegerField(blank=False, default=22,verbose_name="主机port")
    resource_password = models.CharField(max_length=250, blank=False, verbose_name="主机password")
    resource_rsa = models.TextField(blank=True, verbose_name="主机Rsa密钥")
    creator = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, verbose_name="创建人")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    modified_date = models.DateTimeField(auto_now=True, verbose_name="修改时间")

    class Meta:
        verbose_name = _('资源')
        verbose_name_plural = _('资源池')

    def __str__(self):
        return self.resource_hostname
