address = {
    "Shyam" :{
    "age":36,
    "city":"Irving"
},
    "Mowni":{
        "age":33,
        "city":"Dallas"
    }
}

import json
j = json.dumps(address,indent=2)
with open("jsonexample.txt","w") as f:
    f.write(j)

with open("jsonexample.txt","r") as r:
    s = r.read()
    data = json.loads(s)
print(data["Shyam"]["city"])