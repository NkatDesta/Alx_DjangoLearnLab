from django.http import HttpResponse
from .forms import BookSearchForm

def index(request):
    return HttpResponse("Welcome to the Book Shelf!")

# Safe input handling

def search_books(request):
    form = BookSearchForm(request.GET or None)
    results = []
    if form.is_valid():
        query = form.cleaned_data['query']
        results = Book.objects.filter(title__icontains=query)
    return render(request, 'bookshelf/book_list.html', {'form': form, 'results': results})


