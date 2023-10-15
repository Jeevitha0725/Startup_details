import requests
from bs4 import BeautifulSoup

search_query = "Business idea Registeration"
search_url = f"https://www.google.com/search?q={search_query}"

response = requests.get(search_url)
soup = BeautifulSoup(response.content, "html.parser")

result_divs = soup.find_all("div", attrs={"class": "Gx5Zad fP1Qef xpd EtOod pkphOe"})
Details={"Website_name":[],"Web_link":[],"Site_type":[]}
for con in result_divs:
    # print(con)
    Link=con.find("a").get("href")
    l=con.find("a")
    # print(l)
    link=str(Link).split("/")
    print(link[3])
    Name=con.find("div",attrs={"class":"BNeawe UPmit AP7Wnd lRVwie"}).text
    name=str(Name).split(".")
    N=str(link[3]).split("www.")
    # print(N[1])
    # print(link[2])
    # print(name[1])
    Type=Name.split(" ")
    print(Type[2])
    Details["Website_name"].append(N[1])
    Details["Web_link"].append(link[3])
    Details["Site_type"].append(Type[2])
print(Details)