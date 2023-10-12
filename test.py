from utils.functions import xhr

data = xhr("get", "https://google.com", headers={}, headers={})
print (data.text)