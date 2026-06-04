from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tasks.models import Task
from django.utils import timezone
import datetime
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def dashboard_home(request):
    start_date_str = request.GET.get('start_date')
    end_date_str = request.GET.get('end_date')

    tasks = Task.objects.all()

    if start_date_str:
        try:
            start_date = datetime.datetime.strptime(start_date_str, '%Y-%m-%d').date()
            tasks = tasks.filter(created_at__date__gte=start_date)
        except ValueError:
            pass
            
    if end_date_str:
        try:
            end_date = datetime.datetime.strptime(end_date_str, '%Y-%m-%d').date()
            tasks = tasks.filter(created_at__date__lte=end_date)
        except ValueError:
            pass

    # Basic stats
    total_tasks = tasks.count()
    status_counts = tasks.values('status').annotate(count=Count('status'))
    
    stats = {
        'total': total_tasks,
        Task.Status.REGISTERED: 0,
        Task.Status.PENDING: 0,
        Task.Status.IN_PROGRESS: 0,
        Task.Status.COMPLETED: 0,
        'overdue': 0
    }
    
    for item in status_counts:
        stats[item['status']] = item['count']

    # Calculate overdue
    today = timezone.now().date()
    stats['overdue'] = tasks.exclude(status=Task.Status.COMPLETED).filter(due_date__lt=today).count()

    context = {
        'stats': stats,
        'start_date': start_date_str,
        'end_date': end_date_str,
    }
    return render(request, 'dashboard/index.html', context)


@login_required
def mapa_operativo(request):
    return render(request, "dashboard/mapa_operativo.html")