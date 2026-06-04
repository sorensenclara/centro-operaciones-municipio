from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from dashboard import views as dashboard_views
from tasks import views as tasks_views
from dashboard.views import mapa_operativo


urlpatterns = [

    # Admin
    path('admin/', admin.site.urls),

    # Auth
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='accounts/login.html'
        ),
        name='login'
    ),

    path(
        'logout/',
        auth_views.LogoutView.as_view(
            next_page='login'
        ),
        name='logout'
    ),

    # Dashboard
    path(
        '',
        dashboard_views.dashboard_home,
        name='dashboard'
    ),

    # Mapa Operativo
    path(
        'mapa-operativo/',
        mapa_operativo,
        name='mapa_operativo'
    ),

    # Kanban
    path(
        'kanban/',
        tasks_views.kanban_board,
        name='kanban'
    ),

    # Tasks
    path(
        'tasks/',
        tasks_views.TaskListView.as_view(),
        name='task_list'
    ),

    path(
        'tasks/create/',
        tasks_views.task_create,
        name='task_create'
    ),

    path(
        'tasks/<int:pk>/',
        tasks_views.TaskDetailView.as_view(),
        name='task_detail'
    ),

    path(
        'tasks/<int:pk>/edit/',
        tasks_views.task_update,
        name='task_update'
    ),

    path(
        'tasks/<int:pk>/delete/',
        tasks_views.TaskDeleteView.as_view(),
        name='task_delete'
    ),

    path(
        'tasks/update_status/',
        tasks_views.update_task_status,
        name='update_task_status'
    ),

    # Articles
    path(
        'articles/',
        tasks_views.ArticleListView.as_view(),
        name='article_list'
    ),

    path(
        'articles/create/',
        tasks_views.ArticleCreateView.as_view(),
        name='article_create'
    ),

    path(
        'articles/<int:pk>/edit/',
        tasks_views.ArticleUpdateView.as_view(),
        name='article_update'
    ),

    path(
        'articles/<int:pk>/delete/',
        tasks_views.ArticleDeleteView.as_view(),
        name='article_delete'
    ),
]