import json


if __name__ == "__main__":
    with open('selection.json') as f:
        data = json.load(f)

        icons = data['icons']

        print(len(icons))

        charmap = {}

        for icon in icons:
            properties = icon['properties']
            name = properties['name']
            code = properties['code']
            charmap[name] = hex(code)
        
        charmap_string = json.dumps(charmap, indent=4)

        with open('charmap.json', 'w') as f:
            f.write(charmap_string)