from django.http import HttpResponse


def index(request):
    context = 'У меня получилось!'
    return HttpResponse('У меня получилось???')


def second_page(request):
    return HttpResponse('А это вторая страница')
