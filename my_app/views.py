from django.shortcuts import render, redirect

def home_view(request):
    return render(request, 'home.html')

def about_view(request):
    return render(request, 'about.html')

def contact_view(request):
    if request.method == 'POST':
        # ფორმის მონაცემები (შემდეგისთვის)
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        return redirect('thank_you')
    return render(request, 'contact.html')

def thank_you_view(request):
    return render(request, 'thank_you.html')
