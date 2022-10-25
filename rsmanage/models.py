from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


# Create your models here.

class Resource(models.Model):
    """
    QA机器资源DB模型
    """
    resource_hostname = models.CharField(max_length=250, blank=False, verbose_name="主机hostname")
    resource_ip = models.GenericIPAddressField(protocol='both', verbose_name="主机ip")
    resource_port = models.SmallIntegerField(blank=False, default=22, verbose_name="主机port")
    resource_password = models.CharField(max_length=250, blank=False, verbose_name="主机password")
    resource_rsa = models.TextField(blank=True, verbose_name="主机Rsa密钥")
    creator = models.ForeignKey(User, null=True, on_delete=models.SET_NULL,
                                verbose_name="创建人")
    last_editor = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name="last_editor",
                                    verbose_name="最后编辑者")
    # last_editor = models.CharField(max_length=256, blank=True, verbose_name='最后编辑者')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    modified_date = models.DateTimeField(auto_now=True, verbose_name="修改时间")

    class Meta:
        verbose_name = _('资源')
        verbose_name_plural = _('资源池')

        permissions = [
            ("import", "Can import resource pool"),
            ("export", "Can export resource pool"),
        ]

    def __str__(self):
        return self.resource_hostname


class RFConfig(models.Model):
    """
    RF使用的orch配置的DB模型
    """
    orchestrator_name = models.CharField(max_length=250, blank=False)
    json_info = models.JSONField(verbose_name="json_info")

    class Meta:
        verbose_name = _('配置')
        verbose_name_plural = _('RF使用的Orch配置')

    def __str__(self):
        return self.orchestrator_name


class CaseDisplay(models.Model):
    """
    自动化Case展示 DB模型
    包含 Suite Name, Case Name, Tag Name, Documentation字段
    """
    # suite_name =
    # case_name =
    # tag_name =
    # documentation =
