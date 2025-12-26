from django.urls import path
from . import views

app_name = 'mysaving'

urlpatterns = [
    path('',views.mysaving_home,name="mysaving_home"),
    path('expense/',views.mysaving_expense,name="mysaving_expense"),
    path('income/',views.mysaving_income,name="mysaving_income"),
    path('expenseView/<int:id>/',views.expenseView,name='expenseView'),
    path('expenseEdit/<int:id>/',views.expenseEdit,name='expenseEdit'),
    path('incomeView/<int:id>/',views.incomeView,name='incomeView'),
    path('incomeEdit/<int:id>/',views.incomeEdit,name='incomeEdit'),
    path('incomeDelete/<int:id>',views.incomeDelete,name='incomeDelete'),
    path('expenseDelete/<int:id>',views.expenseDelete,name='expenseDelete'),

]
