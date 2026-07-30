import urllib.request

try:
    req = urllib.request.Request('http://localhost:3000/dashboard')
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
        if 'AgentVerse' in html and 'Marketplace' in html and 'Pipelines' in html:
            print("Sidebar IS present in HTML")
            if 'w-64' in html:
                print("Sidebar has w-64 class")
            else:
                print("Sidebar missing w-64 class!")
        else:
            print("Sidebar IS NOT present in HTML")
            print(html[:500])
except Exception as e:
    print(f"Error fetching page: {e}")
