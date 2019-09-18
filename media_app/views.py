from django.shortcuts import render,redirect
from .forms import DocumentForm
from .models import Document
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from accounts.models import CustomUser
from .models import Friend
from django.contrib import messages
from django.db.models import Q
from django.views import generic
from django.urls import reverse_lazy

class up_load(generic.CreateView):
    # アップロード
    def get_form_kwargs(self, *args, **kwargs):
        form_kwargs = super().get_form_kwargs(*args, **kwargs)
        form_kwargs['initial'] = {'author': self.request.user}  # フォームに初期値を設定する。
        return form_kwargs

    model = Document
    form_class = DocumentForm
    success_url = reverse_lazy('home')
    template_name = 'media_app/up_load.html'

# def up_load(request):
#     #POSTauthorが空の時はできない
#     #form = DocumentForm(request.POST, request.FILES,{'author': request.user})
#     if request.method == 'POST':
#         form = DocumentForm(request.POST, request.FILES,{'author': request.user})
#         if form.is_valid():
#             #form.save(commit=false)
#             print("debug01")
#             form.author = request.user
#             print(form.author)
#             form.save()
#             return redirect('home')
#             #return HttpResponseRedirect('')#レダイレクト先はhome画面へ遷移
#     else:
#         print("debug02")
#         form = DocumentForm()
#     return render(request, 'media_app/up_load.html', {'form': form,'author': request.user})

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

# Friendの追加処理
def add(request):
    # 追加するUserを取得
    add_name = request.GET['name']
    add_user = CustomUser.objects.filter(username=add_name).first()
    # Userが本人だった場合の処理
    print("debug01")
    if add_user == request.user:
        messages.info(request, "自分自身をFriendに追加することはできません。")
        return redirect(to='view')
    # publicの取得
    #(public_user, public_group) = get_public()
    # add_userのFriendの数を調べる
    print("debug02")
    frd_num = Friend.objects.filter(owner=request.user).filter(friend=add_user).count()
    # ゼロより大きければ既に登録済み
    if frd_num > 0:
        messages.info(request, add_user.username + ' は既に追加されています。')
        return redirect(to='view')

    # ここからFriendの登録処理
    print("debug03")
    frd = Friend()
    frd.owner = request.user
    frd.friend = add_user
    #frd.group = public_group
    frd.save()
    # メッセージを設定
    messages.success(request, add_user.username + ' を追加しました！ groupページに移動して、追加したFriendをメンバーに設定して下さい。')
    return redirect(to='view')
