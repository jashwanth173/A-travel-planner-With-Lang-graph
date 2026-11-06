from tools.Taavily import tavily_search
from tools.flight import search_flights

#res = tavily_search("best hotels in india")
#print(res)
res = search_flights("plan a 7 days india trip")
print(res)