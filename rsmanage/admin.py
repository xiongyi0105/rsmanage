from django.contrib import admin
from rsmanage.models import Resource
from django.http import HttpResponse


# Register your models here.

def import_csv_to_model(modeladmin, request, queryset):
    response = HttpResponse(content="text/csv")


class ResourceAdmin(admin.ModelAdmin):
    exclude = ('creator',)
    list_display = ('resource_hostname', 'resource_ip', 'resource_port', 'creator', 'created_date', 'modified_date')

    def save_model(self, request, obj, form, change):
        obj.creator = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Resource, ResourceAdmin)
