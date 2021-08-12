from django.contrib import messages
from django.core.mail import EmailMultiAlternatives, BadHeaderError
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.template import RequestContext

from sitemanager.models import Blogs, BlogImage, PortfolioImages, MapSection, ContactInfo, ProfileImage, CarouselImage


def index(request):
    p_img = ''
    p_info = ''

    p_infos = ContactInfo.objects.all()
    for p_info in p_infos:
        p_info = p_info

    p_imgs = ProfileImage.objects.all()[:1]
    for p_img in p_imgs:
        p_img = p_img

    context = {
        'p_info': p_info,
        'p_img': p_img
    }

    return render(request, 'index.html', context)


def about(request, id):
    p_info = ''
    p_img = ''
    c_imgs1 = ''
    c_imgs = ''
    p_infos = ContactInfo.objects.all()

    p_imgs = ProfileImage.objects.filter(img_caption="aboutIMG")
    for p_img in p_imgs:
        p_img = p_img

    for p_info in p_infos:
        p_info = p_info

    c_imgs1 = CarouselImage.objects.all()[:1]
    c_imgs = CarouselImage.objects.all()[1:]

    context = {
        'p_info': p_info,
        'p_img': p_img,
        'c_imgs1': c_imgs1,
        'c_imgs': c_imgs
    }
    return render(request, 'about.html', context)


def contact(request):
    emt_map = ''
    p_info = ''
    emt_map = MapSection.objects.all()
    p_infos = ContactInfo.objects.all()

    for p_info in p_infos:
        p_info = p_info

    if request.method == 'POST':
        client_name = request.POST['fullname']
        client_phone = request.POST['phoneno']
        client_email = request.POST['email']
        message = request.POST['message']

        myemail = "jayeshnandgaonkar10@gmail.com"
        mysubject = client_email
        my_text_content = '' + client_name + '/ ' + client_phone + '/ ' + client_email + '/ ' + message + ' '
        my_html_content = '<div><p>name : ' + client_name + ' <br>Phone No: ' + client_phone + '<br>Email: ' + client_email + '<br>Message: ' + message + ' </p></div>'

        try:
            my_msg = EmailMultiAlternatives(mysubject, my_text_content, myemail, [myemail])
            my_msg.attach_alternative(my_html_content, "text/html")
            my_msg.send()
        except BadHeaderError:
            messages.success(request, 'Please Reload And Try Again!')
            return HttpResponseRedirect(request.path)

        messages.success(request, 'Thanks for contacting us! We will be in touch with you shortly.')
        return HttpResponseRedirect(request.path)

    context = {
        'emt_maps': emt_map,
        'p_info': p_info
    }

    return render(request, 'contact.html', context)


def blogs(request):
    blogs = ''
    photos = ''
    p_info = ''
    blogs = Blogs.objects.filter(blog_publish=True)

    p_infos = ContactInfo.objects.all()

    for p_info in p_infos:
        p_info = p_info

    for blog in blogs:
        post = get_object_or_404(Blogs, id=blog.id)
        photos = BlogImage.objects.filter(blog=post)

    context = {'blogs': blogs,
               'photos': photos,
               'p_info': p_info

               }

    return render(request, 'blogs.html', context)


def singleblog(request, single_blog):
    blogs = ''
    photos = ''
    p_info = ''

    blogs = Blogs.objects.filter(blog_slug=single_blog)

    p_infos = ContactInfo.objects.all()

    for p_info in p_infos:
        p_info = p_info

    for blog in blogs:
        post = get_object_or_404(Blogs, id=blog.id)
        photos = BlogImage.objects.filter(blog=post)

    context = {'blogs': blogs,
               'photos': photos,
               'p_info': p_info

               }

    return render(request, 'singleblog.html', context)


def facilities(request):
    p_info = ''
    p_infos = ContactInfo.objects.all()

    for p_info in p_infos:
        p_info = p_info

    context = {
        'p_info': p_info
    }
    return render(request, 'facilities.html', context)


def portfolio(request):
    p_info = ''
    portfolio_obj = ''
    p_infos = ContactInfo.objects.all()

    for p_info in p_infos:
        p_info = p_info
    portfolio_obj = PortfolioImages.objects.filter(publish_status=True)

    context = {
        'portfolio_objs': portfolio_obj,
        'p_info': p_info
    }

    return render(request, 'portfolio.html', context)


def testimonial(request):
    p_info = ''
    p_infos = ContactInfo.objects.all()
    for p_info in p_infos:
        p_info = p_info

    context = {
        'p_info': p_info
    }

    return render(request, 'testimonial.html', context)


def testfunction(request):
    thisisdata = "this is data"
    p_infos = ContactInfo.objects.all()

    ctx = {'p_infos': p_infos}
    return render(request, 'testtemp.html', ctx)
