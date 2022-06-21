from django.shortcuts import render

from webapp.check_value import Check, ErrorValueRange, ErrorValueSet, ErrorValueDeficiency


def form_vie(request):
    secret_nums = [5, 1, 2, 9]
    if request.method == 'GET':
        return render(request, "index.html")
    else:
        print(request.POST)
        value = request.POST.get("numbers")
        try:
            number_int = Check.check_int(value)
            Check.check_values(number_int)
            Check.check_set(number_int)
            Check.check_num(number_int, secret_nums)
            bulls, cows = Check.sum_bulls(number_int, secret_nums)
            if bulls == 4:
                number_int = "You got it right!"
            else:
                number_int = f"Bulls:{bulls} Cows:{cows}"
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


# Create your views here.
