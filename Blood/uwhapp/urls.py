from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^donor_logincheck/',views.DonorLogincheck.as_view()),
    url(r'^donor',views.DonorPage.as_view()),
    url(r'^bloodbank_logincheck/', views.BloodbankLogincheck.as_view()),
    url(r'^bloodbank/', views.Bloodbank.as_view()),
    url(r'', views.Index.as_view()),
]
