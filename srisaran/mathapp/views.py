from django.shortcuts import render
import math

def surfacearea(request):
    context = {
        'area': 0,
        'r': 0,
        'h': 0
    }

    if request.method == 'POST':
        r = request.POST.get('radius', 0)
        h = request.POST.get('height', 0)

        try:
            r = float(r)
            h = float(h)

            area = 2 * math.pi * r * (h + r)

            context = {
                'area': round(area, 2),   # cleaner output
                'r': r,
                'h': h
            }

        except:
            # if user enters wrong input
            context = {
                'area': "Invalid Input",
                'r': r,
                'h': h
            }

    return render(request, 'mathapp/math.html', context)