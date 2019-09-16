from django.shortcuts import render,redirect
from .forms import DocumentForm
from .models import Document
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from accounts.models import CustomUser
#from accounts.forms import CustomUserCreationForm
#from accounts.models import CustomUser
# Create your views here.

def up_load(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            #form.save(commit=false)
            form.author = request.user
            form.save()
            return redirect('home')
            #return HttpResponseRedirect('')#レダイレクト先はhome画面へ遷移
    else:
        form = DocumentForm()
    return render(request, 'media_app/up_load.html', {'form': form,'author': request.user})

def view(request):
    obj = Document.objects.all()
    paginator = Paginator(obj, 5) # 1ページに10件表示
    p = request.GET.get('p') # URLのパラメータから現在のページ番号を取得
    objs = paginator.get_page(p) # 指定のページのArticleを取得
    params = {
        'title': 'view',
        'objs': objs,
    }
    return render(request,'media_app/view.html',params)
