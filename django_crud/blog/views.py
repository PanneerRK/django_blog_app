from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from .models import Post, AboutUs, Subcategory, Category
import logging
from django.http import Http404
from django.core.paginator import Paginator
from .forms import ContactForm
from django.core.mail import send_mail
from django.http import JsonResponse

# Create your views here.
def index(request):
    blog_title = "Latest posted"
    #Get data from post model
    all_posts = Post.objects.all()
    paginator = Paginator(all_posts, 6)
    page_number = request.GET.get('page')
    page_obj =  paginator.get_page(page_number)
    return render(request, "blog/index.html", {"blog_title": blog_title, 'page_obj': page_obj})

def detail(request, slug):
    # post = next((item for item in posts if item['id'] == int(post_id)), None)
    # logger = logging.getLogger("TESTING")
    # logger.debug(f'Post variable is {post}')
    try:
        #Get data from model by using post ID
        post = Post.objects.get(slug=slug)
        related_posts = Post.objects.filter(category = post.category).exclude(pk=post.id)
    except Post.DoesNotExist:
        raise Http404("Post Does Not Exist!")
    return render(request, "blog/detail.html", {'post': post, "related_posts":related_posts})

def old_url_redirect(request):
    return redirect(reverse("blog:new_page_url"))

def new_url_view(request):
    return HttpResponse("This is the new url")

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # logger = logging.getLogger("TESTING")
        subject = f"New Contact Form Submission from {name}"
        full_message = f"Message:\n{message}\n\nFrom: {name}\nEmail: {email}"
        if form.is_valid():
            send_mail(subject, full_message, email, ['webwizardsusa@gmail.com'])
            # logger.debug(f'Post data is {form.cleaned_data['name']} {form.cleaned_data['email']} {form.cleaned_data['message']}')
            success_message = "Your email is sent successfully"
            return render(request, "blog/contact.html", {'form':form, 'success_message':success_message})
        else:
            # logger.debug('Form is invalid')
            return render(request, "blog/contact.html", {'form':form, 'name':name, 'email':email, 'message':message})
    return render(request, "blog/contact.html")

def about_view(request):
    about_content = AboutUs.objects.first().content
    return render(request, "blog/about.html", {'about_content':about_content})

def get_subcategories(request):
    category_id = request.GET.get('category_id')
    if category_id:
        # Get only the subcategories that belong to the selected category
        subcategories = Subcategory.objects.filter(category_id=category_id)
        # Return the subcategories as JSON
        data = {
            'subcategories': [{'id': sub.id, 'name': sub.name} for sub in subcategories]
        }
        return JsonResponse(data)
    return JsonResponse({'subcategories': []})  # Return empty if no category_id is provided