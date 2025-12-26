from django.urls import path
from . import views

app_name = 'dad'

urlpatterns = [
    path('',views.dad_home,name="dad_home"),
    path('expense/',views.dad_expense,name="dad_expense"),
    path('income/',views.dad_income,name="dad_income"),
    path('expenseView/<int:id>/',views.expenseView,name='expenseView'),
    path('expenseEdit/<int:id>/',views.expenseEdit,name='expenseEdit'),
    path('incomeView/<int:id>/',views.incomeView,name='incomeView'),
    path('incomeEdit/<int:id>/',views.incomeEdit,name='incomeEdit'),
    path('incomeDelete/<int:id>',views.incomeDelete,name='incomeDelete'),
    path('expenseDelete/<int:id>',views.expenseDelete,name='expenseDelete'),

]
