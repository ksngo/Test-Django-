
from django.contrib import admin
from django.urls import path, include
import reviews.views

urlpatterns = [
   
    path('', reviews.views.index, name="show_reviews_route"),
    path('create/<book_id>', reviews.views.create, name="create_review_route"),
    path("update/<review_id>", reviews.views.update_review, name = 'update_review_route'),
    path("delete/<review_id>", reviews.views.delete_review, name= 'delete_review_route'),
    path("details/<review_id>", reviews.views.view_review_details, name="view_review_details_route"),
    path("comment/create/<review_id>", reviews.views.process_create_comment, name="process_create_comment_route")
]
