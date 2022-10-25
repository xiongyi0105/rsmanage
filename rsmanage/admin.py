from django.contrib import admin
from django.contrib.admin.options import csrf_protect_m
from django.shortcuts import render
from rsmanage.form import RFConfigChangeView
from rsmanage.models import Resource, RFConfig
from import_export.admin import ImportExportModelAdmin
from import_export import resources

from django.db import router, transaction

from django.http import HttpResponseRedirect


# Register your models here.

# 自定义Admin actions,批量修改按钮重定向至view：/admin/rsmanage/update/
def bulk_editing(modeladmin, request, queryset):
    print(request.POST)
    return HttpResponseRedirect("/admin/rsmanage/update/", )


bulk_editing.short_description = "批量修改"


# 定义导入导出功能的resource,将在注册的admin中使用
class RsmanageResource(resources.ModelResource):
    class Meta:
        model = Resource
        fields = ('id', 'resource_hostname', 'resource_ip', 'resource_port', 'resource_password', 'resource_rsa')


class RFConfigAdmin(admin.ModelAdmin):
    """
    RFConfig模型的Admin页面定制（“RF使用的Orch配置”模块）
    """
    list_filter = ("orchestrator_name",)
    # 原来的change表单模板无法显示json格式，重写change_form
    change_form_template = 'rfconfig_change_form.html'

    # 定制extra_context参数,对重写的change_form传入所需的自定义模板上下文
    @csrf_protect_m
    def changeform_view(self, request, object_id=None, form_url="", extra_context=None):
        obj_ins = RFConfig.objects.filter(id=object_id)
        extra_context = {
            'rfconfig': RFConfigChangeView(initial=list(obj_ins.values())[0])}
        with transaction.atomic(using=router.db_for_write(self.model)):
            return self._changeform_view(request, object_id, form_url, extra_context)


class ResourceAdmin(ImportExportModelAdmin):
    # 详情页排除字段
    exclude = ('creator', 'last_editor')

    # 列表页展示字段
    list_display = (
        'resource_hostname', 'resource_ip', 'resource_port', 'creator', 'last_editor', 'created_date', 'modified_date')

    # 用于搜索的字段
    search_fields = ('resource_hostname', 'resource_ip', 'resource_port')

    # 用于过滤的字段
    list_filter = ('resource_hostname', 'resource_ip', 'resource_port')

    # 显示排序
    ordering = ('resource_hostname',)

    # 自定义actions
    actions = [bulk_editing]

    # ImportExportModelAdmin.
    def save_model(self, request, obj, form, change):
        obj.creator = request.user
        obj.last_editor = request.user
        super().save_model(request, obj, form, change)

    resource_class = RsmanageResource


admin.site.register(Resource, ResourceAdmin)
admin.site.register(RFConfig, RFConfigAdmin)
