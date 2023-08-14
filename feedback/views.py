from django.shortcuts import render
from .models import Feedback
from .forms import FeedbackForm
from django.shortcuts import redirect

# Create your views here.
def upload_feedback(request):
    form = FeedbackForm()
    return render(request, 'feedback/feedback_upload.html', {'form': form})

def upload_feedbacks(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:   
            form = FeedbackForm()   
        return render(request, "feedback/feedback_upload.html", {"form": form})
    
def feedback_list(request): 
    feedbacks = Feedback.objects.all()
    return render(request, "feedback/feedback_list.html", {"feedbacks": feedbacks})

def feedback_details(request, id):
    feedback = Feedback.objects.get(id=id)
    return render(request, "feedback/feedback_detail.html",{"feedback":feedback})

def edit_feedback_view(request, id):
    feedback = Feedback.objects.get(id=id)
    if request.method == "POST":
        form = FeedbackForm(request.POST, instance=feedback)
        if form.is_valid():
            form.save()
            return redirect('feedback_detail_view', id=feedback.id)
    else:
        form = FeedbackForm(instance=feedback)
    return render(request, "feedback/edit_feedback.html", {"form": form})

