import requests

# print(requests.get("http://127.0.0.1:8000/").json())
# print(requests.get("http://127.0.0.1:8000/items/3").json())
# print(requests.get("http://127.0.0.1:8000/items/1").json())
# print(requests.get("http://127.0.0.1:8000/items/asas").json())
# print(requests.get("http://127.0.0.1:8000/items?name=Nails").json())

print("Adding an item")
print(
    requests.post(
        "http://127.0.0.1:8000",
        json={"name": "Screwdriver", "price": 3.99, "count": 10, "id": 4, "category": 'Tools'},
    ).json()
)
print(requests.get("http://127.0.0.1:8000/").json())
print("")

print("updating an item")
print(requests.put("http://127.0.0.1:8000/items/2?count=9092").json())
print(requests.get("http://127.0.0.1:8000/").json())
print()

print("delete an item")
print(requests.delete("http://127.0.0.1:8000/items/2").json())
print(requests.get("http://127.0.0.1:8000/").json())
print()

print(requests.get("http://127.0.0.1:8000/items?category=abcd").json())