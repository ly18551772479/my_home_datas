from django.shortcuts import render
from django.core.cache import cache
from .nodeinfo import get_context
import os
from NodeInfo.settings import BASE_DIR


def Info(request):
    context = cache.get('data')
    if not context:
        print('---no cache --------')
        context = get_context()
        cache.set('data', context, 3600)
    file_path = os.path.join(BASE_DIR, 'templates/nodeinfo.html')
    with open(file_path, 'r+') as f:
        f.seek(0)
        f.truncate()
        f.write(context)
    return render(request, 'nodeinfo.html', )
