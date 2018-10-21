import datetime

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from dateutil.relativedelta import relativedelta

# Use /hello-world URL
def hello_world(request):
    """Return a 'Hello World' string using HttpResponse"""
    return HttpResponse('Hello World')


# Use /date URL
def current_date(request):
    """
        Return a string with current date using the datetime library.

        i.e: 'Today is 5, January 2018'
    """
    return HttpResponse('Today is ' + datetime.date.today().strftime("%d, %B %Y"))


# Use URL with format /my-age/<year>/<month>/<day>
def my_age(request, year, month, day):
    """
        Return a string with the format: 'Your age is X years old'
        based on given /year/month/day datetime that come in the URL.

        i.e: /my-age/1992/1/20 returns 'Your age is 26 years old'
    """
    year, month, day = int(year), int(month), int(day)
    if month not in range(1,13) or day not in range(1,31): 
        return HttpResponseBadRequest("Invalid month/day format. Please try again with the format: /my-age/<year>/<month>/<day> ")
    time_now = datetime.datetime.now()
    dob = datetime.datetime(year, month, day, 0,0)
    yrs = relativedelta(time_now, dob).years

    return HttpResponse('Your age is ' + str(yrs) + ' years old')


# Use URL with format /next-birthday/<birthday>
def next_birthday(request, birthday):
    """
        Return a string with the format: 'Days until next birthday: XYZ'
        based on a given string GET parameter that comes in the URL, with the
        format 'YYYY-MM-DD'
    """

    try:
        year, month, day = birthday.split('-')
        year, month, day = int(year), int(month), int(day)
        datetime.datetime(year, month, day)
    except ValueError:
        return HttpResponseBadRequest("Invalid birthday format. <br>Please try again with format /next_birthday/YYYY-MM-DD ")

    now = datetime.datetime.now()
    future_date = datetime.datetime(int(now.year)+1, month, day)
    diff = future_date - now
    return HttpResponse('Days untill next birthday: ' + str(diff.days) + ' days')

# Use /profile URL
def profile(request):
    """
        This view should render the template 'profile.html'. Make sure you return
        the correct context to make it work.
    """
    return render(request, 'profile.html', {
        'my_name' : 'Pradeep',
        'my_age' : 67
        })



"""
    The goal for next task is to practice routing between two URLs.
    You will have:
        - /authors --> contains a list of Authors (template is provided to you)
        - /author/<authors_last_name> --> contains the detail for given author,
        using the AUTHORS_INFO provided below.

    First view just have to render the given 'authors.html' template sending the
    AUTHORS_INFO as context.

    Second view has to take the authors_last_name provided in the URL, look for
    for the proper author info in the dictionary, and send it as context while
    rendering the 'author.html' template. Make sure to complete the given
    'author.html' template with the data that you send.
"""
AUTHORS_INFO = {
    'poe': {
        'full_name': 'Edgar Allan Poe',
        'nationality': 'US',
        'notable_work': 'The Raven',
        'born': 'January 19, 1809',
    },
    'borges': {
        'full_name': 'Jorge Luis Borges',
        'nationality': 'Argentine',
        'notable_work': 'The Aleph',
        'born': 'August 24, 1899',
    }
}

# Use provided URLs, don't change them
def authors(request):
    return render(request, 'authors.html', {
        'authors_info' : AUTHORS_INFO
        })


def author(request, authors_last_name):
    author = AUTHORS_INFO[authors_last_name]
    full_name  = author['full_name']
    nationality = author['nationality']
    born = author['born']
    notable_work = author['notable_work']

    return render(request, 'author.html', {
        'full_name' : full_name,
        'nationality' : nationality,
        'born' : born,
        'notable_work' : notable_work
        })
