
from django.contrib import admin
from django.urls import path, include
import reviews.views

urlpatterns = [
   
    path('', reviews.views.index, name="show_reviews_route"),
    path('create', reviews.views.create),
    path("update/<review_id>", reviews.views.update_review, name = 'update_review_route'),
    path("delete/<review_id>", reviews.views.delete_review, name= 'delete_review_route')
    
]
