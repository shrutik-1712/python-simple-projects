import validators
import urllib.request as urllib

def website(url):
    print("Checking connectivity ")
    
    response = urllib.urlopen(url)
    print("Connected to" , url, "succesfully")
    print("The response code was: ", response.getcode())

print("This is a site connectivity checker program")
input_url = input("Input the url of the site you want to check: ")
if validators.url(input_url)==True:
    print("valid URL")
    website(input_url)
else:
    print("invaild url")