
from django import forms
color_choices = (("124", "Red"),
("125", "White"),
("126", "Rose"),
("123", "Sparkling"),
("128", "Dessert")
)


varietal_choices = (("138", "Red:  Merlot"),
("139", "Red:  Cabernet Sauvignon"),
("197", "Red:  Cabernet Franc"),
("143", "Red:  Pinot Noir"),
("146", "Red:  Syrah"),
("163", "Red:  Sangiovese"),
("170", "Red:  Nebbiolo"),
("144", "Red:  Bordeaux"),
("169", "Red:  Tempranillo"),
("10079", "Red:  Malbec"),
("141", "Red:  Zinfandel"),
("140", "White:  Chardonnay"),
("141", "White:  Sauvignon Blanc"),
("153", "White:  Riesling"),
("194", "White:  Pinot Gris"),
("10087", "White:  Gruner Veltliner"),
("166", "White:  Gewurztraminer"),
("177", "White:  Semillon"),
("15443", "White:  Trebbiano")
)

region_choices = (("106780", "Oregon"),
("106983", "Washington"),
("106870", "California - All"),
("106882", "California - Napa"),
("106924", "California - Sonoma"),
("107033", "France:  All"),
("107078", "France:  Bordeaux"),
("107034", "France:  Burgandy"),
("107115", "France:  Rhone"),
("107115", "France:  Loire"),
("107074", "France:  Champaigne"),
("107072", "France:  Longuidoc-Roussillon"),
("106806", "Spain:  All"),
("106818", "Spain:  Rioja"),
("1068816", "Spain:  Ribera del Duero"),
("107185", "Italy:  All"),
("107219", "Italy:  Tuscany"),
("107186", "Italy:  Piedmont"),
("107208", "Italy:  Sicily"),
("107209", "Italy:  Sardinia"),
("107008", "Argentina"),
("107136", "Australia"),
("107025", "Austria"),
("107171", "Chile"),
("106828", "Germany"),
("107017", "Portugal"),
("106997", "South Africa")
)



sort_choices = (("?sortBy=topRated", "Rating"),
                ("-702", "90+ Rating"),
                ("-703", "94+ Rating"),
                 ("?sortBy=priceLowToHigh", "Price:  Low to High"),
                  ("?sortBy=priceHighToLow", "Price:  High to Low"),
("?sortBy=oldToNew", "Vintage (Old to New)"),
("?sortBy=newToOld", "Vintage (New to Old)")
)

class ColorForm(forms.Form):
    color_form = forms.ChoiceField(widget=forms.RadioSelect, choices=color_choices)

class VarietalForm(forms.Form):
    varietal_form = forms.ChoiceField(widget=forms.RadioSelect, choices=varietal_choices)

class RegionForm(forms.Form):
    region_form = forms.ChoiceField(widget=forms.RadioSelect, choices=region_choices)

class SortForm(forms.Form):
    sort_form = forms.ChoiceField(widget=forms.RadioSelect, choices=sort_choices)
  