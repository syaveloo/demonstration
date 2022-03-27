import requests


with open("/home/alan/Documents/paths.txt", 'r') as f:
	imgs = f.read().split(";")

l = len(imgs)
for i in range(891, l):
	response = requests.get(imgs[i])
	if response.status_code == 200:
	    with open(f"/home/alan/Documents/imgs/{i}.jpeg", 'wb') as f:
	        f.write(response.content)
	        print(f"{i}/{l}")

