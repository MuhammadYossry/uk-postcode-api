from django.conf.urls import url

from .views import UKPostcodeValidateView

urlpatterns = [
    url(r'^validate/$',
        UKPostcodeValidateView.as_view(),
        name='validate_uk_postcode'),
]
