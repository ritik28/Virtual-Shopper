from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = "store"

urlpatterns = [
    path("", views.product_all, name="store_home"),
    path("<slug:slug>", views.product_detail, name="product_detail"),
    path("shop/<slug:category_slug>/", views.category_list, name="category_list"),
    path(
        "store/apology.html",
        TemplateView.as_view(template_name="store/apology.html"),
        name="COVID_Schedule",
    ),
]
