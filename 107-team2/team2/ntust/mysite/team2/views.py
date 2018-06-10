from django.shortcuts import render_to_response
from django.shortcuts import render
from team2.models import *
# Create your views here.
def index(request):
    m_type = M_Type.objects.all()
    area = Area.objects.all()
    about = About.objects.all()
    museum = Museum.objects.all()
    home = home_page.objects.all()

    content = {'home':home,'museum':museum,'m_type':m_type,'area':area,'about':about}
    return render(request, 'team2/showimg.html', content)

def post_detail1(request):
    m_type = M_Type.objects.all()
    area = Area.objects.all()
    about = About.objects.all()
    museum = Museum.objects.all()
    home = home_page.objects.all()

    content = {'home':home,'museum':museum,'m_type':m_type,'area':area,'about':about}
    return render(request, 'team2/my.html', content)

def post_area(request, pk):
    m_type = M_Type.objects.all()
    area1 = Area.objects.all()
    about = About.objects.all()
    museum = Museum.objects.all()
    home = home_page.objects.all()
    area = Area.objects.get(pk=pk)
    content = {'home':home,'museum':museum,'m_type':m_type,'area':area,'about':about,'area1':area1}
    
    return render(request, 'team2/area.html', content)
def post_about(request):
    m_type = M_Type.objects.all()
    area = Area.objects.all()
    about = About.objects.all()
    museum = Museum.objects.all()
    home = home_page.objects.all()
    content = {'home':home,'museum':museum,'m_type':m_type,'area':area,'about':about}
    
    return render(request, 'team2/about.html', content)
def post_museum(request, pk):
    m_type = M_Type.objects.all()
    area = Area.objects.all()
    about = About.objects.all()
    home = home_page.objects.all()
    museum = Museum.objects.get(pk=pk)
    content = {'home':home,'museum':museum,'m_type':m_type,'area':area,'about':about}
    
    return render(request, 'team2/museum.html', content)
def post_m_type(request, pk):
    m_type1 = M_Type.objects.all()
    area = Area.objects.all()
    about = About.objects.all()
    museum = Museum.objects.all()
    home = home_page.objects.all()
    m_type = M_Type.objects.get(pk=pk)
    content = {'home':home,'museum':museum,'m_type':m_type,'area':area,'about':about,'m_type1':m_type1}

    return render(request, 'team2/m_type.html', content)

def comment(request,pk):

    m_type = M_Type.objects.all()
    area = Area.objects.all()
    about = About.objects.all()
    home = home_page.objects.all()
    museum = Museum.objects.get(pk=pk)
    museum1 = Museum.objects.all()
    user = ''
    content = ''
    if request.method == 'POST':
        content = request.POST.get('content')
        user = request.POST.get('user')
       
        Comment.objects.create(user=user, content=content,museum=museum)

    com = Comment.objects.all()
    
    b= {'content': content,'com':com,'user':user,'museum':museum,'area':area,'about':about,'home':home,'m_type':m_type}
    return render(request, 'team2/comments.html', b)