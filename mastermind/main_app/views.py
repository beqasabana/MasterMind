from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.http import JsonResponse
from random import randint
from random import shuffle
import requests

# Create your views here.
def index(request):
    return render(request, 'main_index.html')

def play(request, code_length=4, duplicates=1, range_start=0, range_end=7, tries=10):
    request.session.clear()
    request.session['hints'] = []
    request.session['max'] = range_end
    if duplicates == 1:
        request.session['code'] = requests.get(f'https://www.random.org/integers/?num={code_length}&min={range_start}&max={range_end}&col=1&base=10&format=plain&rnd=new').text.split()
    elif duplicates == 0:
        request.session['code'] = requests.get(f'https://www.random.org/integer-sets/?sets=1&num={code_length}&min={range_start}&max={range_end}&seqnos=off&commas=off&order=index&format=plain&rnd=new').text.split()
    request.session['attempts'] = tries
    game_settings = {
        'code_length': [i for i in range(code_length+1) if i > 0],
        'min': range_start,
        'max': range_end,
        'code_elements': range(range_end+1)
    }
    return render(request, 'main_play.html', game_settings)

def check(request):
    response = []
    player_input = list(request.POST.values())
    player_input.pop(0)

    for i in range(len(player_input)):
        if player_input[i] == request.session['code'][i]:
            response.append('correct-dot')
        elif player_input[i] in request.session['code']:
            response.append('position-dot')
        else:
            response.append('wrong-dot')
    # sorting the respones so it does not mirror players input
    response.sort()
    # reduce attempts
    request.session['attempts'] -= 1

    # game lost case
    if request.session['attempts'] <= 0:
        return JsonResponse({'status': 0})

    # game won case
    if request.session['code'] == player_input:
        return JsonResponse({'status': 2})

    print('code to brake', request.session['code'])
    print(player_input)
    print(response)
    print(request.session['attempts'])

    return JsonResponse({'status': 1, 'results': response, 'player_input': player_input})

def victory(request):
    return render(request, 'main_victory.html')

def lost(request):
    return render(request, 'main_lost.html')

def customize_display(request):
    return render(request, 'main_customize.html')

def customize_play(request):
    return redirect(f"/play/{request.POST['code_length']}/{request.POST['duplicates']}/{request.POST['range_start']}/{request.POST['range_end']}/{request.POST['tries']}")

# helper function for hints
def generate_hint(previous_hints, max_number, code):
    hint = None
    random_position = randint(0, len(code)-1)
    possible_numbers = list(range(max_number + 1))
    shuffle(possible_numbers)
    for i in possible_numbers:
        if code[random_position] != i:
            hint = f"Position {random_position + 1} is not {i}"
            break
    if hint in previous_hints or hint == None:
        generate_hint(previous_hints, max_number, code)
    return hint

def give_hint(request):
    hints_in_session = request.session['hints']
    hint = generate_hint(hints_in_session, request.session['max'], request.session['code'])
    hints_in_session.append(hint)
    request.session['hints'] = hints_in_session
    return JsonResponse({'hint': hint})