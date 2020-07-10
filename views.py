from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup

# Create your views here.
render_list = []

def scrape_domain(domain):
    """
    Uses Requests and BeautifulSoup to scrape website.
    Scans for all H5 tags which contains the useful doman information.
    Each H5 tag is appened to a list.
    Function returns domain and list into a new function.
    """
    base = "https://check-mail.org/domain/"
    url = base+domain
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    domain_data = []
    for h5 in soup.find_all("h5"):
        values = h5.text
        domain_data.append(values)
    
    return print_domain_details(domain, domain_data)

def print_domain_details(domain, domain_data):
    """
    Loops over list that is passed into function, checking for a specific tag.
    Domain and tag are added to a dictionary if found.
    Domain is added by itself if no tag is found.
    Dictionaries is appened to a global list which is rendered on the home page.
    """
    domain_dict = {}
    for i in domain_data:
        if i == "Disposable: Yes":
            domain_dict["domain"] = domain
            domain_dict["disposable"] = "DISPOSABLE"
        elif i == "Disposable: No":
            domain_dict["domain"] = domain
    render_list.append(domain_dict)

def index(request):
    """
    Renders the default home.html page by default.
    Checks for search form being submitted on home page, reads data and sends it to other functions.
    Returned data is rendered back to home page into a table.
    """
    context = None
    if request.method == "POST":
        # Clear list on new load
        render_list.clear()
        domains = request.POST.get("textfield", None).split()

        for domain in domains:
            scrape_domain(domain)

        # Render user submitted context on same page
        context = {"render_list" : render_list}
        return render(request, "pages/home.html", context)
    return render(request, "pages/home.html", context)