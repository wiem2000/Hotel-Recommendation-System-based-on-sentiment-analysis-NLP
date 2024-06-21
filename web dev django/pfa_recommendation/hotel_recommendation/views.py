from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
import requests
from hotel_recommendation.models import Hotel, User
from django.shortcuts import render
from django.contrib import messages

from django.shortcuts import render, get_object_or_404


def home(request):

    username = request.session.get('username')

    hotels=Hotel.objects.all()
    paginator = Paginator(hotels, 15)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "index.html", {"hotels": page_obj,'username':username})

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username, password=password)
            # Stocker l'utilisateur dans la session
            request.session['username'] = user.username
            return redirect('recommendations')
        except User.DoesNotExist:
            messages.error(request, 'Nom d’utilisateur ou mot de passe incorrect')
            return render(request, 'login.html')
    return render(request, 'login.html')


def get_user_interests(interests):
    
        # Récupérer l'utilisateur
      
        
        # Vérifier les intérêts de l'utilisateur
        user_interests = interests.lower()
        
        interests =[]
        # Associer des intérêts à des valeurs spécifiques
        if 'breakfast' in user_interests or 'food' in user_interests or 'properties' in user_interests :
            interests.append('health care')
        if 'place' in user_interests or 'location' in user_interests or 'accommodation' in user_interests or 'room' in user_interests :
            interests.append('event homes and garden')
        if 'foot' in user_interests or 'basket' in user_interests or 'sport' in user_interests :
            interests.append('Physical exercise')
     

        return interests
        

def recommendations_view(request):
    
    username = request.session.get('username')
    if username:
        print(username)
        user = User.objects.get(username=username)
        interests=get_user_interests(user.aspects)

        base_url='http://0d01-34-16-177-172.ngrok-free.app'
        response= requests.post(base_url+'/get', data={'username': username})
        response_hotels= requests.post(base_url+'/get_similar_hotels', data={'username': username})
        response_users= requests.post(base_url+'/get_similar_users', data={'username': username})
        #response_interests= requests.post(base_url+'/get_interests', data={'username': username})

        if response.status_code == 200:
            
            response.encoding = 'utf-8'
            response_users.encoding= 'utf-8'
            response_hotels.encoding= 'utf-8'
            #response_interests.encoding= 'utf-8'
            
            
            
            result = response.json()
            result2= response_users.json()
            similar_hotels_data = response_hotels.json()[:10]
            #interests= response_interests.json()
            
            

            #hotels = Hotel.objects.filter(hotel_name__in=result)[:5]

            #hotels = Hotel.objects.all()[:5]
            users = User.objects.filter(username__in=result2)[:5]
            #users = User.objects.all()[:10]

            hotels = []
            hotels_to_exclude = ["Wetterdelle", "B&B Sapere"]

    
            for hotel_name, aspects in result:
                if hotel_name not in hotels_to_exclude:
                    hotel = get_object_or_404(Hotel, hotel_name=hotel_name)
                    hotels.append({
                        'hotel': hotel,
                        'aspects': aspects
                    })

            labels = []
            data = []



            for h in similar_hotels_data:
                labels.append(h[0])
                data.append(h[1])

            print(labels)
            

        
            return render(request, 'recommendations.html', {
                'user':user,
                'username':username,
                'hotels': hotels,
                'users': users,
                'labels': labels,
                'data':data,
                'interests':interests,

            })
            
        else:
            return HttpResponse("Une erreur s'est produite lors de la communication avec Google Colab.")

    else:
        return redirect('login')


def logout_view(request):
    try:
        del request.session['username']
    except KeyError:
        pass
    return redirect('home')

