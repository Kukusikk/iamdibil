from django.shortcuts import render

# Create your views here.
def post_list(request):
    # return render(request, '/home/fuckinggirl/Рабочий стол/iamdolboyasher/myproject/templatpost_list.html', {})
    return render(request, 'post_list.html', {})