from django.shortcuts import  redirect, render
from .forms import EmployeeForm # type: ignore
from .models import Employee # type: ignore

def listEmployee(request):
    context = {'employees': Employee.objects.all()}
    return render(request, 'listemployee.html', context)



def addEmployee(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, 'addemployee.html', {'form': form})
    
    elif request.method == "POST":
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST, instance=employee)
        
        if form.is_valid():
            form.save()
            return redirect('listEmployee')
    
    return render(request, 'addemployee.html', {'form': form})

def deleteEmployee(request, id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('listEmployee')
