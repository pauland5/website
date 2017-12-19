from django.shortcuts import render
from django.http import HttpResponse





def select_wine(data):
    
    data ="ppppppp"
    
 
    return(data)


# Create your views here.
def index(request):
    import requests
    from .forms import ColorForm, NameForm   
   
    current_name = "Not Specified"
    color_selected = ""
  

    

    
    region_dict = {"California":"5654", "Oregon":"3333", "Washington":"6666"}
    wine_color_dict = {"Red":"59494", "Rose":"93838", "White":"182828", "Sparkling":"4828283","Desert":"383838"}
    varietal_dict = {"Cabernet":"8867","Claret":"1422","Merlot":"78678","Zinfandel":"56456"}
    sort_dict = {"Highest Rated":"5344","Most Popular":"6454", "Lowest Price":"68484"}

    name_form = NameForm(request.POST or None)
    color_form = ColorForm(request.POST or None)
    if request.method == "POST":
        # Have Django validate the form for you
        if color_form.is_valid():
            # The "display_type" key is now guaranteed to exist and
            # guaranteed to be "displaybox" or "locationbox"

            color_selected = color_form.cleaned_data
             
    # This will display the blank form for a GET request
    # or show the errors on a POSTed form that was invalid
    else:
        color_form = ColorForm()



    baseurl = 'https://www.wine.com/list/wine/'
    country = 'spain/'
    wine_color = 'red-wine/'
    varietal = 'tempranillo/'
    code = '7155-106806-124-169'
    sortby = '?sortBy=topRated' 

  
    return render(request, 'wine/home.html', {'color_form': color_form}, {'name_form': name_form})


def results(request):


    import requests
    import re

    baseurl = 'https://www.wine.com/list/wine/'
    country = 'spain/'
    wine_color = 'red-wine/'
    varietal = 'tempranillo/'
    code = '7155-106806-124-169'
    sortby = '?sortBy=topRated' 

    url = baseurl + country + wine_color + varietal + code + sortby
    quote_data = requests.get(url)
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
        appellation = appellation_text[0]
        #print (appellation)
        wine_list.append(appellation)

        #Get Name
        split_raw_data = wine.split('fullName"')
        name_raw_data = split_raw_data[1]
        string = ':"(.+?)",'
        name_text = re.findall(string, name_raw_data)
        name = name_text[0]
        #print (name)
        wine_list.append(name)

        #Get Rating
        split_raw_data = wine.split('professionalReviews"')
        review_raw_data = split_raw_data[1]
        string = 'rating":(.+?),"'
        rating_text = re.findall(string, review_raw_data)
        rating = rating_text[0]
        #print (rating)
        wine_list.append(rating)

        #Get Price
        split_raw_data = wine.split('regularPrice"')
        price_raw_data = split_raw_data[1]
        string = 'display":"(.+?)"'
        price_text = re.findall(string, price_raw_data)
        #print(price_text[0])
        try:
            price = float(price_text[0])
        except:
            price =0.0
        wine_list.append(price)
  
        #Get Vineyard
        split_raw_data = wine.split('vineyard"')
        vineyard_raw_data = split_raw_data[1]
        string = 'fullName":"(.+?)"'
        vineyard_text = re.findall(string, vineyard_raw_data)
        vineyard = vineyard_text[0]
        #print(vineyard)
        wine_list.append(vineyard)

        #Get Varietal
        split_raw_data = wine.split('varietal"')
        varietal_raw_data = split_raw_data[1]
        string = 'shortDesc":"(.+?)"'
        varietal_text = re.findall(string, varietal_raw_data)
        varietal = varietal_text[0]
        #print(varietal)
        wine_list.append(varietal)

        #Get Vintage
        split_raw_data = wine.split('vintage"')
        vintage_raw_data = split_raw_data[1]
        string = ':"(.+?)"'
        vintage_text = re.findall(string, vintage_raw_data)
        vintage = vintage_text[0]
        #print(vintage)
        wine_list.append(vintage)

        #Get Region
        split_raw_data = wine.split('region"')
        region_raw_data = split_raw_data[1]
        string = ':"(.+?)"'
        region_text = re.findall(string, region_raw_data)
        region = region_text[0]
        #print(region)
        wine_list.append(region)

        #Get Description
        split_raw_data = wine.split('longDescription"')
        description_raw_data = split_raw_data[1]
        string = ':"(.+?)"'
        description_text = re.findall(string, description_raw_data)
        description = description_text[0]
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

        #Get Lat and Long
        split_raw_data = wine.split('geoLat"')
        try:
            geo_raw_data = split_raw_data[1]
            string = ':(.+?),'
            lat_text = re.findall(string, geo_raw_data)
            lattitude = lat_text[0]

            string = 'geoLong":(.+?),'
            long_text = re.findall(string, geo_raw_data)
            longitude = long_text[0]

        except:
            lattitude = "N/A"
            longitude = "N/A"

        #print(lattitude, longitude)
        wine_list.append(lattitude)
        wine_list.append(longitude)

        dict[wine_count] =wine_list
    
    wine_dict = dict
    #wine_dict ={"1":"aaaaa","2":"bbbbbbbbbb","3":"ccccccc"}
    
    data_hold = wine_dict
    
    item_list = list()
    for x in range(0,10):
        item_list.append(x)

    context = {"var1":"Nothing Specified", "var2":"Data Exists", "var3":item_list, "wine_list": data_hold}

    return render(request, 'wine/results.html', context)


def details(request):
    return HttpResponse("<h1>Below are the details for the wine you selected</h1>")

