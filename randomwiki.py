print('Random Wikipedia article catcher | Arfur')
print('--'*20)

def get_page():
    import requests
    import re
    title = requests.get('https://wikipedia.org/wiki/Special:Random')
    t = title.text
    global d
    d = re.search('<\W*title\W*(.*)</title', t, re.IGNORECASE)
    return d.group(1)

def go_to_page():
    import webbrowser
    p = str(d.group(1)).replace(' - Wikipedia','')
    webbrowser.open_new_tab('https://wikipedia.org/wiki/' + p)

print(get_page())
while True:
    r = str(input('Visit article? [Y/N]'))[0]
    if r not in 'YyNnSs01':
        while r not in 'YyNnSs01':
            r = str(input('Visit article? [Y/N]'))[0]
    if r in 'Nn0':
        print(get_page())
    if r in 'YySs1':
        go_to_page()
        print(get_page())
