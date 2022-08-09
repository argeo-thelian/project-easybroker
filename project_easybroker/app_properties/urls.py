from django.urls import path
from . import views 
# defaults.page_not_found(request, exception, template_name='404.html')

app_name = 'easybroker'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('<int:page>', views.HomeView.as_view(), name='home'),
    path('property/<str:property_id>', views.PropertyView.as_view(), name='property'),
    path('property/<str:property_id>/<str:status>', views.PropertyView.as_view(), name='property'),
    path('contact/<str:property_id>', views.ContactView, name='contact'),

]