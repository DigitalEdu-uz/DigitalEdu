from django.shortcuts import render
from django.views.generic.base import View
from .models import Course, Category


class MainView(View):
    """Основная страница"""
    def get(self, request):

    	# Филтруеть посты если пост не черновык то выведёт пост
        query = Course.objects.filter(draft=False).order_by('-created_at')
        categories = Category.objects.all()
        

        return render(request, 'main/index.html',
    		{'nav_name': 'Основная страница',
            'course_list': query,
            'view': {'category': categories}})