from collections import Counter

from django.shortcuts import render

counter_show = Counter()
counter_click = Counter()


def index(request):
    if request.GET.get('from-landing') == 'original':
        counter_click['original_click'] += 1
        return render(request, 'index.html')
    elif request.GET.get('from-landing') == 'test':
        counter_click['test_click'] += 1
        return render(request, 'index.html')
    else:
        return render(request, 'index.html')



def landing(request):
    if request.GET.get('ab-test-arg') == 'original' or request.GET.get('ab-test-arg') == None:
        counter_show['original_show'] += 1
        return render(request, 'landing.html')
    else:
        counter_show['test_show'] += 1
        return render(request, 'landing_alternate.html')


def stats(request):
    return render(request, 'stats.html', context={
        'test_conversion': counter_click['test_click'] / counter_show['test_show'],
        'original_conversion': counter_click['original_click'] / counter_show['original_show'],
    })
