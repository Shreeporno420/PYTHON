import pygal
#Chart
chart = pygal.Pie()
chart.title = "Favourite Pet"
chart.add("Dog", 6)
chart.add("Cat", 4)
chart.add("Hamster", 3)
chart.add("Fish", 2)
chart.add("Snake", 1)
chart.render()

#Chart Bar
bar = pygal.Bar()
bar.add("Dog", 6)
bar.add("Cat", 4)
bar.add("Hamster", 3)
bar.add("Fish", 2)
bar.add("Snake", 1)

bar.render()