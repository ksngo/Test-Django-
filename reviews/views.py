from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from .models import Review
from .forms import ReviewForm

# Create your views here.
def index(request):

    reviews = Review.objects.all()


    return render(request, "reviews/index.template.html", {
        "reviews" :reviews
    })

@login_required
def create(request):

    if request.method == 'POST' :
        retrieved_reviews_form=ReviewForm(request.POST)

        if retrieved_reviews_form.is_valid():

            phantom_form = retrieved_reviews_form.save(commit=False)
            phantom_form.user = request.user
            temporary_variable = phantom_form.save()
            messages.success(request, f"reviews for {phantom_form.book} has been created")

            return redirect(reverse(index))
        
        else:
            return render(request, 'reviews/create.template.html', {
            'form' : create_reviews_form
            })

    else: 
        create_reviews_form = ReviewForm()

        return render(request, 'reviews/create.template.html', {
        'form' : create_reviews_form
        })


@login_required
def update_review(request, review_id):

    retrieved_review_object_by_id = get_object_or_404(Review, pk=review_id)

    if request.method == 'POST' :

        retrieved_review_object_form = ReviewForm(request.POST, instance=retrieved_review_object_by_id)

        if retrieved_review_object_form.is_valid():
            retrieved_review_object_form.save()
            return redirect(reverse(index))
        else:
            retrieved_review_form = ReviewForm(instance=retrieved_review_object_by_id)

            return render(request, "reviews/update.template.html", {
            "form" : retrieved_review_form
            })


    else:
    
        retrieved_review_form = ReviewForm(instance=retrieved_review_object_by_id)

        return render(request, "reviews/update.template.html", {
            "form" : retrieved_review_form
            })


@login_required
def delete_review(request, review_id):

    retrieved_review_object_by_id = get_object_or_404(Review, pk=review_id)

    if request.method == "POST" :

        retrieved_review_object_by_id.delete()

        return redirect(reverse(index))
    else:

        return render(request, "reviews/delete_review.template.html", {
            "review_to_delete" : retrieved_review_object_by_id
            })

    




