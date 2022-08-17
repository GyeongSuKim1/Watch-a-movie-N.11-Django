import json

with open('tag.json', 'r') as f:
    tag_list = json.load(f)
# print(tag_list)

new_list = []
for tag in tag_list:
    new_data = {"model": "movie.tag"}
    new_data["fields"] = {}
    new_data["fields"]["tag"] = tag
    new_list.append(new_data)

# print(new_list)

with open('tag_data.json', 'w', encoding='UTF-8') as f:
    json.dump(new_list, f, ensure_ascii=False, indent=2)