"""concierge URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from .views import health_check, api_serializer, KeyTransferView, form_accepted, PersonFormView, \
    PersonListView, PersonDetailView, IndexView

# from .views import healthcheck

urlpatterns = [
    path('admin/', admin.site.urls),
    path('healthcheck/', health_check, name='health_check'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', IndexView.as_view(), name='index'),
    path('api/<str:object_type>/<int:object_id>', api_serializer, name='api-serializer'),

    path('person-form/', PersonFormView.as_view(), name='person-form'),
    path('person-list/', PersonListView.as_view(), name='person-list'),
    # path('person-list/', cache_page(CACHE_TTL)(PersonListView.as_view()), name='person-list'),
    path('person-detail/<int:pk>', PersonDetailView.as_view(), name='person-detail'),

    # TODO
    # path('apartment-form/', ApartmentFormView.as_view(), name='apartment-form'),
    # path('apartment-list/', ApartmentListView.as_view(), name='apartment-list'),
    # path('apartment-detail/<int:pk>', ApartmentDetailView.as_view(), name='apartment-detail'),
    #
    # path('key-transfer-form/', KeyTransferFormView.as_view(), name='key-transfer-form'),
    # path('key-transfer-list/', KeyTransferListView.as_view(), name='key-transfer-list'),
    # path('key-transfer-detail/<int:pk>', KeyTransferDetailView.as_view(), name='key-transfer-detail'),
    #
    # path('key-form/', KeyFormView.as_view(), name='key-form'),
    # path('key-list/', KeyListView.as_view(), name='key-list'),
    # path('key-detail/<int:pk>', KeyDetailView.as_view(), name='person-detail'),

    path('form-accepted/', form_accepted, name='form-accepted'),
    path('key-transfer-form/', KeyTransferView.as_view(), name='key-transfer-form'),

]
