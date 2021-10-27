from rest_framework.viewsets import ViewSet
from core.models import Company
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from core import views
from core.views import CompanyNameViewset
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.DefaultRouter()
router.register("company",views.CompanyViewSet,basename="company")
router.register("companybank", views.CompanyBankViewSet, basename="companybank")
router.register("medicine", views.MedicineViewSet, basename="medicine")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('api/gettoken/',TokenObtainPairView.as_view(),name="gettoken"),
    path('api/resfresh_token/',TokenRefreshView.as_view(),name="refresh_token"),
    path('api/companybyname/<str:name>/',CompanyNameViewset.as_view(),name="companybyname"),
]
