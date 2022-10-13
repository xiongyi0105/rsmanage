from django.contrib import admin
from rsmanage.models import Resource
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from django.http import HttpResponseRedirect


# Register your models here.

# 自定义Admin actions
def bulk_editing(modeladmin, request, queryset):
    # for i in queryset:
    #     print(i.id)
    print(request.POST)
    return HttpResponseRedirect(f"/rsmanage/update/",) # ?queryset={queryset}


bulk_editing.short_description = "批量修改"


# 定义导入导出功能的resource,将在注册的admin中使用
class RsmanageResource(resources.ModelResource):
    class Meta:
        model = Resource
        fields = ('id', 'resource_hostname', 'resource_ip', 'resource_port', 'resource_password', 'resource_rsa')


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
