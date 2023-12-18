import json
from django.shortcuts import render

file = open("data.json", "r", encoding="utf8")
text = file.read()
file.close()
data = json.loads(text)

file = open("users.json", "r", encoding="utf8")
text = file.read()
file.close()
users = json.loads(text)

automobile = []
for auto in data["automobiles"]:
    automobile.append(auto)

keywords = []
for key in users["all_users"]:
    keywords.append(key)

img = {
    0: "https://i.quto.ru/c533x400/5b9780f8055aa.jpeg",
    1: "https://i.quto.ru/c533x400/58985ae15d1ae.jpeg",
    2: "https://i.quto.ru/c533x400/5b895cd5a57c2.jpeg",
    3: "https://i.quto.ru/c533x400/58ff40c43e469.jpeg"
}

def auth(request):
    req = request.GET
    return render(request, 'auth.html', {
        "keywords": keywords,
        "login": req.get("login"),
        "pass": req.get("pass"),
    })

def reg(request):
    req = request.GET
    reg = {}
    reg["login"] = req.get("login")
    reg["password"] = req.get("pass")
    reg["status"] = "user"
    for i in reg:
        if reg.get(i) is None or reg.get(i) == "":
            return render(request, "reg.html")
    users["all_users"].append(reg)
    save_user()
    return render(request, "reg.html")

def main_a(request):
    return render(request, 'main_a.html', {})

def main_u(request):
    return render(request, 'main_u.html', {})

def all_auto(request):
    return render(request, 'all_auto.html', {
        "autos": automobile
    })

def auto(request, autoid):
    if len(img) <= int(autoid):
        return render(request, "auto.html", {
            "point": automobile[int(autoid)],
        })
    return render(request, 'auto.html', {
        "img": img[int(autoid)],
        "point": automobile[int(autoid)],
    })

def description(request):
    return render(request, "about.html", {})

def search(request):
    req = request.GET
    return render(request, "search.html", {
        "autos":automobile,
        "name": req.get("search"),
    })

def redact(request):
    return render(request, "redact.html", {})

def add_auto(request):
    req = request.GET
    car = {}
    car["id"] = req.get("id")
    car["marka"] = req.get("marka")
    car["name"] = req.get("name")
    car["type"] = req.get("type")
    car["date"] = req.get("date")
    car["owner"] = req.get("owner")
    car["description"] = req.get("description")
    for i in car:
        if car.get(i) is None or car.get(i) == "":
            return render(request, "admin/add_auto.html")
    data["automobiles"].append(car)
    save_json()
    return render(request, "admin/add_auto.html", {})

def delete_auto(request):
    req = request.GET
    id = req.get("id")
    for car in data["automobiles"]:
        if id == car["id"]:
            data["automobiles"].remove(car)
    save_json()
    return render(request, 'admin/delete_auto.html', {})

def save_json():
    dbFile = open("data.json", "w", encoding="utf8")
    dbFile.write(json.dumps(data, ensure_ascii=False))
    dbFile.close()

def add_user(request):
    req = request.GET
    use = {}
    use["login"] = req.get("login")
    use["password"] = req.get('password')
    use["status"] = req.get("status")
    for i in use:
        if use.get(i) is None or use.get(i) == "":
            return render(request, "admin/add_user.html")
    users["all_users"].append(use)
    save_user()
    return render(request, "admin/add_user.html", {})

def delete_user(request):
    req = request.GET
    login = req.get("login")
    for i in users["all_users"]:
        if login == i["login"]:
            users["all_users"].remove(i)
    save_user()
    return render(request, 'admin/delete_user.html', {})

def save_user():
    dbfile = open("users.json", "w", encoding="utf8")
    dbfile.write(json.dumps(users, ensure_ascii=False))
    dbfile.close()
