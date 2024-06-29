from django.shortcuts import get_object_or_404, redirect, render
from students.models import Student
from students.forms import StudentForm

def index(request):
    
    students = Student.objects.all()
    context = {'students': students}
    return render(request, "index.html", context)
    
def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, "student_detail.html", {"student": student})


def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = StudentForm()
    
    return render(request, 'student_form.html', {'form': form})


def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'student_form.html', {'form': form})


def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        student.delete()
        return redirect('student_list')
    return render(request, 'student_confirm_delete.html', {'student': student})