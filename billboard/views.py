from lib2to3.fixes.fix_input import context

from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Billboard
from django.shortcuts import render, get_object_or_404
from .forms import BillboardForm

def billboards_list(request):
    billboards = Billboard.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'billboard/billboards_list.html', {'billboards': billboards})

def billboards_detail(request,pk):
    billboard = get_object_or_404(Billboard, pk=pk)
    return render(request, 'billboard/billboards_detail.html', {'billboard': billboard,'is_admin_panel':True})

def billboard_new(request):
    if request.method == "POST":
        form = BillboardForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('billboards_detail', pk=post.pk)
    else:
        form = BillboardForm()
        return render(request, 'billboard/billboards_edit.html', {'form': form, 'is_admin_panel':True})

def billboards_edit(request,pk):
    post = get_object_or_404(Billboard, pk=pk)
    if request.method == "POST":
        form = BillboardForm(request.POST,instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('billboards_detail', pk=post.pk)
    else:
        form = BillboardForm(instance=post)
        return  render(request,'billboard/billboards_edit.html', {'form': form})


def admin_panel(request):
    billboards = Billboard.objects.all()
    return render(request, 'billboard/admin_panel.html',{'billboard': billboards,'is_admin_panel':True})