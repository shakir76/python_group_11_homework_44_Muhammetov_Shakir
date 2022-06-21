from django.shortcuts import render

from webapp.check_value import Check, ErrorValueRange, ErrorValueSet, ErrorValueDeficiency

STEP = []
MESSAGE = []
WALK = 0


def form_vie(request):
    secret_nums = [5, 1, 2, 9]

    if request.method == 'GET':
        return render(request, "index.html")
    else:
        value = request.POST.get("numbers")
        try:
            number_int = Check.check_int(value)
            Check.check_values(number_int)
            Check.check_set(number_int)
            Check.check_num(number_int, secret_nums)
            global WALK
            WALK += 1
            global STEP
            STEP.append(WALK)
            bulls, cows = Check.sum_bulls(number_int, secret_nums)
            if bulls == 4:
                number_int = "You got it right!"
            else:
                number_int = f"Bulls:{bulls} Cows:{cows}"
            global MESSAGE
            MESSAGE.append(number_int)
        except ValueError:
            number_int = "Error value not int"
        except ErrorValueRange:
            number_int = "Error value not range 1,9"
        except ErrorValueSet:
            number_int = "Error repeating elements"
        except ErrorValueDeficiency:
            number_int = "Error deficiency elements"
        context = {
            'numbers': number_int
        }
        return render(request, "index.html", context)


def history(request):
    global STEP
    global MESSAGE
    context = {
        'step': STEP,
        'message': MESSAGE
    }
    return render(request, "history.html", context)

# Create your views here.
