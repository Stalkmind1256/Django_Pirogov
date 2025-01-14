from lib2to3.fixes.fix_input import context

from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Billboard
from django.shortcuts import render, get_object_or_404
from .forms import BillboardForm
from django.http import JsonResponse
from django.http import HttpResponseForbidden

def billboards_list(request):
    billboards = Billboard.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'billboard/billboards_list.html', {'billboards': billboards})

def billboards_detail(request,pk):
    billboard = get_object_or_404(Billboard, pk=pk)
    return render(request, 'billboard/billboards_detail.html', {'billboard': billboard})

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

def billboards_edit(request, pk):
    post = get_object_or_404(Billboard, pk=pk)
    if request.method == "POST":
        form = BillboardForm(request.POST, instance=post)
        if form.is_valid():
            updated_post = form.save(commit=False)
            if request.user == post.author or request.user.is_superuser:
                updated_post.save()
                return redirect('billboards_detail', pk=updated_post.pk)
            else:
                return HttpResponseForbidden("Вы не можете редактировать это объявление.")
    else:
        form = BillboardForm(instance=post)
    return render(request, 'billboard/billboards_edit.html', {'form': form})


def admin_panel(request):
    billboards = Billboard.objects.all()
    return render(request, 'billboard/admin_panel.html',{'billboard': billboards,'is_admin_panel':True})

def billboard_delete(request, pk):
    billboard = get_object_or_404(Billboard, pk=pk)
    billboard.delete()
    return redirect('billboards_list')

def billboards_manage(request):
    billboards = Billboard.objects.all()
    return render(request, 'billboard/billboards_manage.html', {'billboards': billboards})

def billboard_delete_ajax(request):
    if request.method == "POST":
        billboard_id = request.POST.get('id')
        try:
            billboard = Billboard.objects.get(id=billboard_id)
            billboard.delete()
            return JsonResponse({'success': True})
        except Billboard.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Объявление не найдено'})
    return JsonResponse({'success': False, 'error': 'Неверный метод запроса'})