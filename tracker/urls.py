from django.urls import path
from . import views

app_name = 'tracker'

urlpatterns = [
    path('',views.tracker_home,name="tracker_home"),
    path('expense/',views.tracker_expense,name="tracker_expense"),
    path('income/',views.tracker_income,name="tracker_income"),
    path('expenseView/<int:id>/',views.expenseView,name='expenseView'),
    path('expenseEdit/<int:id>/',views.expenseEdit,name='expenseEdit'),
    path('incomeView/<int:id>/',views.incomeView,name='incomeView'),
    path('incomeEdit/<int:id>/',views.incomeEdit,name='incomeEdit'),
    path('incomeDelete/<int:id>',views.incomeDelete,name='incomeDelete'),
    path('expenseDelete/<int:id>',views.expenseDelete,name='expenseDelete'),

]
