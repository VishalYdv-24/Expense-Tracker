from django.shortcuts import render,redirect
from .models import Expense, Income
from .forms import ExpenseForm,IncomeForm
from datetime import date
# Create your views here.


from django.db.models import Sum

# views.py
from datetime import date
from django.db.models import Sum
from .models import Expense, Income

def tracker_home(request):
    today = date.today()

    # Read from GET, fallback to current month/year
    month = int(request.GET.get('month', today.month))
    year = int(request.GET.get('year', today.year))

    # Filter by selected month/year
    expense = Expense.objects.filter(exp_date__month=month, exp_date__year=year)
    income  = Income.objects.filter(inc_date__month=month,  inc_date__year=year)

    total_expense = expense.aggregate(total=Sum('exp_amount'))['total'] or 0
    total_income  = income.aggregate(total=Sum('inc_amount'))['total'] or 0

    return render(request, 'tracker/home.html', {
        'expense': expense,
        'income': income,
        'total_expense': total_expense,
        'total_income': total_income,
        'balance': total_income - total_expense,
        'selected_month': month,
        'selected_year': year,
        'years': range(today.year, 2051),  # till 2050
    })



def tracker_expense(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tracker:tracker_home')
        else:
            print(form.errors)   # 👈 ADD THIS

    form = ExpenseForm()
    return render(request, 'tracker/addExpense.html', {'form': form})


def tracker_income(request):
    if request.method == "POST":
        form = IncomeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tracker:tracker_home')
        else:
            print(form.errors)

    form = IncomeForm()
    return render(request, 'tracker/addIncome.html', {'form': form})
    
def expenseView(request,id):
    expense = Expense.objects.get(id=id)
    context = {
        'expense' : expense
    }
    return render(request,'tracker/expenseView.html',context)

def incomeView(request,id):
    income = Income.objects.get(id=id)
    context = {
        'income' : income
    }
    return render(request,'tracker/incomeView.html',context)

def expenseEdit(request,id):
    expense = Expense.objects.get(id=id)
    if request.method == "POST":
        form = ExpenseForm(request.POST,instance=expense)
        if form.is_valid():
            form.save()
            return redirect('tracker:tracker_home')
    
    form = ExpenseForm(instance=expense)
    context = {
        'form' : form
    }
    return render(request,'tracker/addexpense.html',context)


def incomeEdit(request,id):
    income = Income.objects.get(id=id)
    if request.method == "POST":
        form = IncomeForm(request.POST,instance=income)
        if form.is_valid():
            form.save()
            return redirect('tracker:tracker_home')
    
    form = IncomeForm(instance=income)
    context = {
        'form' : form
    }
    return render(request,'tracker/addincome.html',context)


def expenseDelete(request,id):
    expense = Expense.objects.get(id=id)
    expense.delete()
    return redirect('tracker:tracker_home')

def incomeDelete(request,id):
    income = Income.objects.get(id=id)
    income.delete()
    return redirect('tracker:tracker_home')