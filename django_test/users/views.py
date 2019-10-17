from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views import View
from .models import Info


class IndexView(View):
    def get(self, request):
        print('### IndexView_get #######################')
        return render(request, 'collect_info.html')

    def post(self, request):
        print('### IndexView_post #######################')
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        student = Info()
        print('### name :', name)
        print('### gender :', gender)
        print('### age :', age)
        student.name = name
        student.age = age
        student.gender = gender
        student.save()
        return redirect(reverse('show'))


class ShowInfo(View):
    def get(self, request):
        print('### ShowInfo_get #######################')
        infos = Info.objects.all()
        print('### infos:', infos)
        return render(request, 'show_info.html', {'infos': infos})

    def post(self, request):
        pass
