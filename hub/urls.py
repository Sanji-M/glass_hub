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
    path('settings/',views.settings_view,name='settings'),
    path('todo/create/',views.create_todo,name='todo-create'),
    path('todo/<int:id>/toggle/',views.todo_toggle,name='todo-toggle'),
    path('todo/<int:id>/delete/',views.todo_delete,name='todo-delete'),
    path('memories/',views.memories,name='memories'),
    path('memories/create/',views.memory_create,name='memory-create'),
    path('memories/<int:id>/delete/',views.memory_delete,name='memory-delete'),
    path('memories/<int:id>/colour/',views.memory_update_colour,name='memory-colour')

    ]