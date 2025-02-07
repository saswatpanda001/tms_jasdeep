from django.urls import path, include
from core import views

app_name = "core"

urlpatterns = [
    path('', views.home, name="home" ),
    path('emp/dashboard',views.dashboard,name="emp_dashboard"),
    path('emp/dashboard_mng',views.dashboard_mng,name="mng_dashboard"),
    path('feedback',views.feedback,name="feedback"),
    path('emp/learning',views.learning,name="emp_learning"),
    path('emp/profile',views.profile,name="emp_profile"),
    path('emp/promotion',views.promotion,name="emp_promotion"),
    path('emp/rewards',views.rewards,name="emp_rewards"),
    path('emp/skillgap',views.skillgap,name="emp_skillgap")
]
