





# Press the green button in the gutter to run the script.
import requests

import urllib
import requests


def url_shortener(full_link, link_name):
    API_KEY = "cd6080cba0e6e84b7bf7740d9e3428e1"
    BASE_URL = "https://cutt.ly/api/api.php";
    payload = {"key": API_KEY, "short": full_link, "name": link_name};
    request = requests.get(BASE_URL, params=(payload));
    data = request.json();
   # print(data);
    try:
        title = data['url']['title'];
        short_link = data['url']['shortLink'];
        print("Title : ",title);
        print("Link : ",short_link);
    except:
        status = data["url"]['status'];
        if status== 1 :
            print("Error : ",status," link already shortened");
        elif status == 2:
            print("Error : ", status, " not a link");
        elif status==3:
            print("Error : ", status, " link name already taken");
        elif status == 4:
            print("Error : ", status), " Invalid api key";
        elif status == 5:
            print("Error : ", status, " Not a link");
        elif status == 6:
            print("Error : ", status, " link from blocked domain");
        elif status == 8:
            print("Error : ", status, "You have reached your limit. You can upgrade your subscription plan to add more links.");



link = input("Enter a link ");
name = input("Give your link a name ");

url_shortener(link, name);




