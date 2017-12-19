import requests
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import VarietalForm, RegionForm, SortForm
import re




# Create your views here.
def index(request):
     
    print (request.method)


    if request.method =="POST":
        print('*'*50)
        print(request.POST)
        varietal_form = VarietalForm(request.POST)
        if varietal_form.is_valid():
            varietal_data = varietal_form.cleaned_data
            varietal = varietal_data['varietal_form']
            print("varietal: ", varietal)
        region_form = RegionForm(request.POST)
        if region_form.is_valid():
            region_data = region_form.cleaned_data
            region = region_data['region_form']
            print("region: ", region)
        sort_form = SortForm(request.POST)
        if sort_form.is_valid():
            sort_data = sort_form.cleaned_data
            sort = sort_data['sort_form']
            print("sort: ", sort)

        next_html = 'wine/results.html'
        pass_dict = {'region':region, 'varietal': varietal, 'sort':sort}
        
        #Required doing a model migration to get session table defined
        request.session['search_data'] = pass_dict
        return redirect('results/')

    else:
        next_html = 'wine/home.html'
        varietal_form = VarietalForm()
        region_form = RegionForm()
        sort_form = SortForm()
        
        pass_dict = {'varietal_form':varietal_form, 'region_form':region_form, 'sort_form':sort_form}
        
        return render(request, next_html, pass_dict)

def results(request):
    import requests
    import re

    print ("made it to Results...........................................................................")
    dict = request.session['search_data']
    print(dict)
   
    #https://www.wine.com/list/wine/oregon/red-wine/pinot-noir/7155-124-143-106780?sortBy=topRated
    baseurl = 'https://www.wine.com/list/wine/7155-'
    
    varietal = dict['varietal'] + "-"
    geo = dict['region']
    sortby = dict['sort']

    url = baseurl +  varietal + geo + sortby
    print("URL: ", url)
    quote_data = requests.get(url)
    print("Request Response Code: ", quote_data)
    html = quote_data.text  
 

    #get the wine data information of the html
    string = 'model":{"models":(.+?)"metadata":{"pageIndex'
    raw_wine_data = re.findall(string, html)
    multi_row_data = raw_wine_data[0]

    #Split the multirowdata into individual rows
    string = '{"appellationId":(.+?),"wineClub":{"destination"'
    wine_data_list = re.findall(string, multi_row_data)

    wine_count = 0

    dict ={}

    #Get details for each wine
    for wine in wine_data_list:
        wine_count = wine_count + 1
        wine_list = list()
    
        #Get Appellation
        split_raw_data = wine.split('shortName"')
        appellation_raw_data = split_raw_data[1]
        string = ':"(.+?)"}'
        appellation_text = re.findall(string, appellation_raw_data)
        try:
            appellation = appellation_text[0]
        except:
            appellation = "N/A"
        
        wine_list.append(appellation)

        #Get Name
        split_raw_data = wine.split('fullName"')
        name_raw_data = split_raw_data[1]
        string = ':"(.+?)",'
        name_text = re.findall(string, name_raw_data)
        try:
            name = name_text[0]
        except:
            name = "N/A"
        wine_list.append(name)

        #Get Rating
        split_raw_data = wine.split('professionalReviews"')
        try:
            review_raw_data = split_raw_data[1]
            string = 'rating":(.+?),"'
            rating_text = re.findall(string, review_raw_data)
        
            rating = rating_text[0]
        except:
            rating = "N/A"
        #print (rating)
        wine_list.append(rating)

        #Get Price
        split_raw_data = wine.split('regularPrice"')
        try:
            price_raw_data = split_raw_data[1]
            string = 'display":"(.+?)"'
            price_text = re.findall(string, price_raw_data)
            #print(price_text[0])
    
            price = price_text[0]
        except:
            price =0.0
        wine_list.append(price)
  
        #Get Vineyard
        split_raw_data = wine.split('vineyard"')
        try:
            vineyard_raw_data = split_raw_data[1]
            string = 'fullName":"(.+?)"'
            vineyard_text = re.findall(string, vineyard_raw_data)
        
            vineyard = vineyard_text[0]
        except:
            vineyard = "N/A"
        #print(vineyard)
        wine_list.append(vineyard)

        #Get Varietal
        split_raw_data = wine.split('varietal"')
        try:
            varietal_raw_data = split_raw_data[1]
            string = 'shortDesc":"(.+?)"'
            varietal_text = re.findall(string, varietal_raw_data)
        
            varietal = varietal_text[0]
        except:
            varietal= "N/A"
        #print(varietal)
        wine_list.append(varietal)

        #Get Vintage
        split_raw_data = wine.split('vintage"')
        try:
            vintage_raw_data = split_raw_data[1]
            string = ':"(.+?)"'
            vintage_text = re.findall(string, vintage_raw_data)
        
            vintage = vintage_text[0]
        except:
            vintage = "N/A"
        #print(vintage)
        wine_list.append(vintage)

        #Get Region
        split_raw_data = wine.split('region"')

        try:
            region_raw_data = split_raw_data[1]
            string = ':"(.+?)"'
            region_text = re.findall(string, region_raw_data)
       
            region = region_text[0]
        except:
            region = "N/A"
        #print(region)
        wine_list.append(region)

        #Get Description
        split_raw_data = wine.split('longDescription"')
        try:
            description_raw_data = split_raw_data[1]
            string = ':"(.+?)"'
            description_text = re.findall(string, description_raw_data)
        
            description = description_text[0]
        except:
            description = "N/A"
        #print(description)
        wine_list.append(description)

        #Get Alcohol
        split_raw_data = wine.split('alcohol')
        try: 
            alcohol_raw_data = split_raw_data[1]
            string = 'Percent":(.+?),'
            alcohol_text = re.findall(string, alcohol_raw_data)
            alcohol = alcohol_text[0]
        except:
            alcohol = "Not Specified"
    
        #print(alcohol)
        wine_list.append(alcohol)


        dict[wine_count] =wine_list

    #for k, v in dict.items():
    #    print (k, v)

    context = {"wine_list": dict}
    #print(context)

    return render(request, 'wine/results.html', context)


def details(request):
    return HttpResponse("<h1>Below are the details for the wine you selected</h1>")

