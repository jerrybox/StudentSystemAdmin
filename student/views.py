from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.views import View

from .models import Student
from .forms import StudentModelForm
# Create your views here.


def index(request):
    # students = Student.objects.all()
    students = Student.get_all()
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            student = Student()
            student.name = cleaned_data['name']
            student.sex = cleaned_data['sex']
            student.email = cleaned_data['email']
            student.profession = cleaned_data['profession']
            student.qq = cleaned_data['qq']
            student.phone = cleaned_data['phone']
            student.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = StudentModelForm()

    context = {'students': students,
               'form':form}
    return render(request, 'index.html', context=context)


def index_auto_save(request):
    students = Student.objects.all()
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = StudentModelForm()

    context = {'students': students,
               'form':form}
    return render(request, 'index.html', context=context)


class IndexView(View):

    template_name = 'index.html'

    def get_context(self):
        students = Student.get_all()
        context = {'students': students}
        return context

    def get(self, request):
        form = StudentModelForm()
        context = self.get_context()
        context['form'] = form
        return render(request, self.template_name, context=context)

    def post(self, request):
        form = StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))

        context = self.get_context()
        context['form'] = form
        return render(request, self.template_name, context=context)




