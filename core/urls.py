from django.urls import path, include
from core import views

app_name = "core"

urlpatterns = [
    path('', views.home, name="home" ),
    path('emp/dashboard',views.dashboard,name="emp_dashboard"),
    path('emp/dashboard_mng',views.dashboard_mng,name="mng_dashboard"),
    path('feedback',views.feedback_view,name="feedback"),
    path('submit-feedback/', views.feedback_view, name='submit-feedback'),
    path('emp/learning',views.learning,name="emp_learning"),
    path('emp/trainings',views.trainings,name="emp_trainings"),
     path('emp/reports',views.reports,name="emp_reports"),
    path('emp/talent',views.talent,name="emp_talent"),
    path('emp/profile',views.profile,name="emp_profile"),
    path('emp/promotion',views.promotion,name="emp_promotion"),
    path('emp/rewards',views.recognition_view,name="emp_rewards"),
    path('emp/skillgap',views.skillgap,name="emp_skillgap"),
    path('emp/emp_list',views.employee_list,name="emp_list"),
    path('emp/details/<int:id>',views.employee_details,name="emp_details"),
    path('emp/details/edit/<int:id>',views.edit_profile,name="edit_emp_profile"),
    path('trainings/add', views.add_training, name='add_training'),
    path('send_points/', views.send_points, name='send_points'),
  
    path('notifications/', views.notification_center, name='notification_center'),
    
]
