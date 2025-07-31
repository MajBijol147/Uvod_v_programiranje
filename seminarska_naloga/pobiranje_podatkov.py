import requests

url = "https://www.bach-digital.de/receive/BachDigitalWork_work_00000001"
odziv = requests.get(url).status_code

# število kompozicij v BWV leta 1998
stevilo_kompozicij = 1126

# ustrezna oblika števila, za vpis v url
