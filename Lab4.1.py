import json

def task() -> float:
    filename = "input.json"
    with open(filename) as f:
        json_data = json.load(f)
    #print(json_data)

    summa = sum([item["score"] * item["weight"] for item in json_data])
    return round(summa, 3)


print(task())
