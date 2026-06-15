from django.urls import path
from django.contrib.auth import views as auth_views
from hub import views


#my urls patterns here
urlpatterns = [
    path('login/',auth_views.LoginView.as_view(template_name = 'hub/login.html') ,name='login'),
    path('signup/',views.signup_view,name='signup'),
    path('logout/',auth_views.LogoutView.as_view(next_page='login') ,name='logout'),
    path('',views.dashboard,name='dashboard' ),
    path('board/',views.board_view,name='board'),
    path('settings/',views.settings_view,name='settings')

]