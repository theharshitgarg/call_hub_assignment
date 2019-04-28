from django.conf.urls import url

from mathcompute import views

urlpatterns = [
    url(r'/apis/v1/fibonacci', views.fibonacci_view, name='fibonacci_api'),
    url(r'fibonacci', views.fibonacci_html_view, name='fibonacci_view'),
]
