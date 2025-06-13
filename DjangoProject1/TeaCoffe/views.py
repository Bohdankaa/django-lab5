from django.shortcuts import render

def home_view(request):
    context = {
        'title': 'Головна Сторінка TeaCoffe'
    }
    return render(request, 'TeaCoffe/index.html', context)

def tea_view(request):
    context = {
        'title': 'Наші Чаї'
    }
    return render(request, 'TeaCoffe/tea.html', context)

def coffee_view(request):
    context = {
        'title': 'Наша Кава'
    }
    return render(request, 'TeaCoffe/coffee.html', context)

def about_view(request):
    context = {
        'title': 'Про нас'
    }
    return render(request, 'TeaCoffe/about.html', context)

def contact_view(request):
    context = {
        'title': 'Контакти'
    }
    return render(request, 'TeaCoffe/contact.html', context)