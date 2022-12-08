from django.shortcuts import render, redirect
from data.forms import StudentForm
from django.views.generic import View
from data.models import Student
from django.contrib import messages
# Create your views here.

# class BaseView(View):
#     views = {}

# class HomeView(BaseView):
#     def get(self, request):
#         if request.method == "POST":
#             fm = StudentForm(request.POST)
#             # if fm.is_valid():
#             #     name = fm.changed_data['name']
#             #     email = fm.changed_data['email']
#             #     pw = fm.changed_data['password']
                
#             # stu = Student.objects.create(
#             #     name = name,
#             #     email = email, 
#             #     password = pw
#             # )
#             fm.save()
#             messages.success(request, "Student Create Successfullly!")
#             return redirect('data:home')
#         else:
#             self.views['fm'] = StudentForm()
#         self.views['student'] = Student.objects.all()
#         return render(request, 'student.html', self.views)

def home(request):
    if request.method == "POST":
        fm = StudentForm(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
                
            stu = Student(
            name = name,
            email = email, 
            password = pw
            )
            stu.save()
            messages.success(request, "Student Create Successfullly!")
            return redirect('data:home')
    else:
        fm = StudentForm()
    student = Student.objects.all()
    context = {'student':student, 'fm':fm}
    return render(request, 'student.html',context)


def delete(request,id):
    id = Student.objects.get(pk = id)
    id.delete()
    return redirect('data:home')

def update(request, id):
    id = Student.objects.get(pk = id)
    if request.method == 'POST':
        fm = StudentForm(request.POST, instance=id)
        if fm.is_valid():
            fm.save()
            return redirect('data:home')

    else:
        fm = StudentForm(instance=id)

    return render(request, 'editStudent.html',{'fm':fm})

