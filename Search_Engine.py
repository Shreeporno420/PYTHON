#make sure you run this programe in trinket.
import pygal
search_engine = pygal.Bar()
search_engine.title = "Best Search Engine"
search_engine.add("Chrome", 92.51)
search_engine.add("Bing", 2.83)
search_engine.add("Yahoo!", 1.59)
search_engine.add("Baidu", 1.14)
search_engine.add("DuckDuckGo", 0.5)
search_engine.add("YANDEX", 0.5)
search_engine.render()