from django.shortcuts import render

from collection.models import Audit

# the rewritten view!
def index(request):
    things = Audit.objects.all()

    return render(request, 'index.html', {
        'things': things,
    })
