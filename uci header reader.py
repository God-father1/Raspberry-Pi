import http.client  #importing the http:client lib
conn = http.client.HTTPSConnection("www.uci.edu")   #establishing connection
conn.request("GET", "/")        #declaring request type
r = conn.getresponse()
print(r.status, r.reason) # Prints that the request went through
data = r.read()       #Reading data
print (data[:10000]) #Prints 10000 bytes