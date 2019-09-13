from functools import reduce
import re

# aspect
# current_price
# depth
# depth_b
# hdmi_ports
# height
# height_b
# inches
# internet
# model
# netflix
# previous_price
# refresh
# res_type
# resolution
# screen_format
# screen_type
# tv_type
# usb_ports
# vesa
# vga_ports
# weight
# width
# width_b
# wifi
# youtube


class Item:

    attr_list = [
        "aspect", "current_price", "depth", "depth_b", "hdmi_ports", "height",
        "height_b", "inches", "internet", "model", "name", "netflix",
        "previous_price", "refresh", "res_type", "resolution", "screen_format",
        "screen_type", "tv_type", "usb_ports", "vesa", "vga_ports", "weight",
        "width", "width_b", "wifi", "youtube",
    ]


    def __init__(self, aspect=None, current_price=None, depth=None,
                 depth_b=None, hdmi_ports=None, height=None, height_b=None,
                 inches=None, internet=None, model=None, name=None,
                 netflix=None, previous_price=None, refresh=None,
                 res_type=None, resolution=None, screen_format=None,
                 screen_type=None, tv_type=None, usb_ports=None, vesa=None,
                 vga_ports=None, weight=None, width=None, width_b=None,
                 wifi=None, youtube=None):

        """docstring for __init__"""

        self.aspect = aspect
        self.current_price = current_price
        self.depth = depth
        self.depth_b = depth_b
        self.hdmi_ports = hdmi_ports
        self.height = height
        self.height_b = height_b
        self.inches = inches
        self.internet = internet
        self.model = model
        self.name = name
        self.netflix = netflix
        self.previous_price = previous_price
        self.refresh = refresh
        self.res_type = res_type
        self.resolution = resolution
        self.screen_format = screen_format
        self.screen_type = screen_type
        self.tv_type = tv_type
        self.usb_ports = usb_ports
        self.vesa = vesa
        self.vga_ports = vga_ports
        self.weight = weight
        self.width = width
        self.width_b = width_b
        self.wifi = wifi
        self.youtube = youtube

    def similitude(self, other):
        """docstring for similitude"""

        matches = []
        for att in Item.attr_list:
            ours = getattr(self, att)
            theirs = getattr(other, att)
            if ours is not None and theirs is not None:
                if ours == theirs:
                    matches.append(ours)

        return len(matches)/len(Item.attr_list)


    def __repr__(self):
        """docstring for __repr__"""
        attributes = {att: getattr(self, att) for att in Item.attr_list}
        att_strings = []
        for att, val in attributes.items():
            string = f'{att}={val}'
            att_strings += [string]

        att_strings = ", ".join(att_strings)

        return f"Item({att_strings})"


    @classmethod
    def from_frave(cls, frave):
        """docstring for from_frave

        "Smart TV 50” 4K Ultra HD TCL L50P65": {
        "name": "Smart TV 50” 4K Ultra HD TCL L50P65",
        "current_price": "$ 32.999",
        "previous_price": "$ 39.999",
        "Imagen": {
        "Pulgadas": "50\"",
        "Tipo de resolución": "4K UHD",
        "Resolución": "3840 x 2160 pixeles",
        "Formato de pantalla": "Plano",
        "Tipo de pantalla": "LED"
        },
        "Características grales.": {
        "Smart TV": "Sí",
        "Procesador": "CA *2,1.0GHz"
        },
        "Caracteristicas Smart": {
        "Youtube": "Sí",
        "Netflix": "Sí"
        },
        "Conectividad": {
        "Entradas HDMI": "3",
        "Entradas USB": "3",
        "Conexión a Internet": "Sí"
        },
        "Dimensiones": {
        "Alto": "65,35 cm",
        "Ancho": "112,14 cm",
        "Profundidad": "7,5 cm",
        "Alto (con base)": "71,45 cm",
        "Ancho (con base)": "112,14 cm",
        "Profundidad (con base)": "22,08 cm",
        "Medida VESA": "200x200",
        "Peso": "10,2 Kg"
        },
        "Modelo y origen": {
        "Modelo": "L50P65",
        "Origen": "Argentina"
        }

    """
        attrs = {k: None for k in cls.attr_list}

        attr_map = {
            'current_price': ('current_price',),
            'depth': ('Dimensiones', 'Profundidad'),
            'depth_b': ('Dimensiones', 'Profundidad \(con base\)'),
            'hdmi_ports': ('Conectividad', 'Entradas HDMI'),
            'height': ('Dimensiones', 'Alto'),
            'height_b': ('Dimensiones', 'Alto \(con base\)'),
            'inches': ('Imagen', 'Pulgadas'),
            'internet': ('Conectividad', 'Conexión a Internet'),
            'model': ('Modelo y origen', 'Modelo'),
            'name': ('name',),
            'netflix': ('Caracter[i-í]sticas Smart', 'Netflix'),
            'previous_price': ('previous_price',),
            'res_type': ('Imagen', 'Tipo de resolución'),
            'resolution': ('Imagen', 'Resolución'),
            'screen_format': ('Imagen', 'Formato de pantalla'),
            'screen_type': ('Imagen', 'Tipo de pantalla'),
            'usb_ports': ('Conectividad', 'Entradas USB'),
            'vesa': ('Dimensiones', 'Medida VESA'),
            'weight': ('Dimensiones', 'Peso'),
            'width': ('Dimensiones', 'Ancho'),
            'width_b': ('Dimensiones', 'Ancho \(con base\)'),
            'youtube': ('Caracter[i-í]sticas Smart', 'Youtube'),
        }

        def r(x, y):
            # print(x, y)
            p = re.compile(y, flags=re.I)
            get_key = list(filter(lambda m: m, map(lambda s: p.match(s), x.keys())))
            keys = [i.string for i in get_key]
            first_key = keys[0] if keys else None
            return x.get(first_key, {})

        for att, path in attr_map.items():
            # print(att, path)
            # value = reduce(lambda x, y: x.get(y), path, frave)
            value = reduce(r, path, frave)
            attrs[att] = value

        return cls(**attrs)
