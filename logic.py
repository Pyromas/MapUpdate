import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

def create_map(cities, marker_color='skyblue'):
    """
    Создает карту с городами и заливает континенты и океаны.
    
    Parameters:
    cities (list of tuple): Список городов в формате [(name, (latitude, longitude)), ...]
    marker_color (str): Цвет маркеров городов.
    """
    fig, ax = plt.subplots(figsize=(12, 8))
    m = Basemap(projection='merc', llcrnrlat=-60, urcrnrlat=90, llcrnrlon=-180, urcrnrlon=180, resolution='c')
    m.drawcoastlines()
    m.drawcountries()
    m.fillcontinents(color='lightgreen', lake_color='aqua')
    m.drawmapboundary(fill_color='aqua')

    for city, (lat, lon) in cities:
        x, y = m(lon, lat)
        m.plot(x, y, 'o', markersize=8, color=marker_color)
        plt.text(x, y, city, fontsize=12, ha='right', color=marker_color)

    return fig, ax

def draw_map(fig, ax):
    """
    Рисует карту с городами.
    
    Parameters:
    fig, ax: Объекты matplotlib.figure.Figure и matplotlib.axes.Axes
    """
    plt.show()
