from django.contrib import admin
from rsmanage.models import Resource
from import_export.admin import ImportExportModelAdmin
from import_export import resources


# Register your models here.

class RsmanageResource(resources.ModelResource):
    class Meta:
        model = Resource
        fields = ('id', 'resource_hostname', 'resource_ip', 'resource_port', 'resource_password', 'resource_rsa')


class ResourceAdmin(ImportExportModelAdmin):
    exclude = ('creator',)
    list_display = ('resource_hostname', 'resource_ip', 'resource_port', 'creator', 'created_date', 'modified_date')

    # ImportExportModelAdmin.
    def save_model(self, request, obj, form, change):
        obj.creator = request.user
        super().save_model(request, obj, form, change)

    resource_class = RsmanageResource


admin.site.register(Resource, ResourceAdmin)
