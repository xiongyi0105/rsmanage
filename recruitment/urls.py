"""recruitment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from rsmanage.models import Resource, RFConfig
from rsmanage import views


class ResourceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Resource
        fields = ['resource_hostname', 'resource_ip', 'resource_port', 'resource_password', 'resource_rsa']


class RFConfigSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RFConfig
        fields = ["json_info"]


class ResourceViewSet(viewsets.ModelViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer


class RFConfigViewSet(viewsets.ModelViewSet):
    queryset = RFConfig.objects.all()
    serializer_class = RFConfigSerializer
    lookup_field = "orchestrator_name"


router = routers.DefaultRouter()
router.register(r'resources', ResourceViewSet)
router.register(r'rf_config', RFConfigViewSet)

urlpatterns = [
    # path('grappelli/', include('grappelli.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('admin/rsmanage/update/', views.bulk_editing, name='resmanage-update'),
    path('admin/', admin.site.urls),
]
