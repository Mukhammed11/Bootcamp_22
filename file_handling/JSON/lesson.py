import json

def wr(**kwargs):
    kwargs = json.dumps(kwargs)
    kwargs = json.loads(str(kwargs))
    with open('jsw.json', 'w', encoding='utf-8') as file:
        json.dump(kwargs, file, indent=4, ensure_ascii=False)

num = {
    'gmail': 'mukhammedd111@gmail.com',
    'login': '1234'
}

print(num)