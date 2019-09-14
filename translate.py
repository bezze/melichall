from functools import reduce
import re
import string
from decimal import Decimal

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

        skip_att = ["name", "current_price", "previous_price"]
        N = len(Item.attr_list) - len(skip_att)
        skip_norm = 0

        matches = []
        for att in Item.attr_list:
            if att in skip_att:
                continue
            ours = getattr(self, att)
            theirs = getattr(other, att)
            if ours is not None and theirs is not None:
                skip_norm += 1
                if ours == theirs:
                    matches.append(ours)

        pure = len(matches)/(N - skip_norm)
        raw = len(matches)/N

        return pure, raw


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
            'current_price':     ('current_price',),
            'depth':             ('Dimensiones', 'Profundidad'),
            'depth_b':           ('Dimensiones', 'Profundidad \(con base\)'),
            'hdmi_ports':        ('Conectividad', 'Entradas HDMI'),
            'height':            ('Dimensiones', 'Alto'),
            'height_b':          ('Dimensiones', 'Alto \(con base\)'),
            'inches':            ('Imagen', 'Pulgadas'),
            'internet':          ('Conectividad', 'Conexi[o-ó]n a Internet'),
            'model':             ('Modelo y origen', 'Modelo'),
            'name':              ('name',),
            'netflix':           ('Caracter[i-í]sticas Smart', 'Netflix'),
            'previous_price':    ('previous_price',),
            'res_type':          ('Imagen', 'Tipo de resoluci[o-ó]n'),
            'resolution':        ('Imagen', 'Resoluci[o-ó]n'),
            'screen_format':     ('Imagen', 'Formato de pantalla'),
            'screen_type':       ('Imagen', 'Tipo de pantalla'),
            'usb_ports':         ('Conectividad', 'Entradas USB'),
            'vesa':              ('Dimensiones', 'Medida VESA'),
            'weight':            ('Dimensiones', 'Peso'),
            'width':             ('Dimensiones', 'Ancho'),
            'width_b':           ('Dimensiones', 'Ancho \(con base\)'),
            'youtube':           ('Caracter[i-í]sticas Smart', 'Youtube'),
        }

        parse_map = {
            'current_price':     number_stripper,
            'previous_price':    number_stripper,
            'inches':            number_stripper,
            'height':            number_stripper,
            'height_b':          number_stripper,
            'depth':             number_stripper,
            'depth_b':           number_stripper,
            'width':             number_stripper,
            'width_b':           number_stripper,
            'weight':            number_stripper,
            'usb_ports':         number_stripper,
            'hdmi_ports':        number_stripper,
            'youtube':           yes_no_parser,
            'wifi':              yes_no_parser,
            'netflix':           yes_no_parser,
            'resolution':        reslution_parser,
            'vesa':              reslution_parser,
        }

        def r(x, y):
            p = re.compile(y, flags=re.I)
            get_key = list(filter(lambda m: m, map(lambda s: p.match(s), x.keys())))
            keys = [i.string for i in get_key if len(i.string) == len(i.group())]
            first_key = keys[0] if keys else None
            return x.get(first_key, {})

        for att, path in attr_map.items():
            value = reduce(r, path, frave)
            if isinstance(value, dict) and not value:
                value = None
            if value is not None:
                parser = parse_map.get(att, lambda x: x)
                attrs[att] = parser(value)
            else:
                attrs[att] = value

        return cls(**attrs)

    @classmethod
    def from_garba(cls, garba):
        attrs = {k: None for k in cls.attr_list}

        attr_map = {
            'current_price':     ('current_price',),
            'depth':             ('dimensions', 'Profundidad'),
            'depth_b':           ('dimensions', 'Profundidad \(con base\)'),
            'hdmi_ports':        ('connection', 'HDMI'),
            'height':            ('dimensions', 'Alto'),
            'height_b':          ('dimensions', 'Alto \(con base\)'),
            'inches':            ('screen', 'Pulgadas'),
            'internet':          ('connection', 'Navegaci[o-ó] Internet'),
            'name':              ('name',),
            'netflix':           ('extras', 'Apto Netflix'),
            'previous_price':    ('previous_price',),
            'res_type':          ('screen', 'Resoluci[o-ó]n de v[i-í]deo'),
            'resolution':        ('screen', 'Resoluci[o-ó]n'),
            'screen_format':     ('screen', 'Formato de pantalla'),
            'screen_type':       ('screen', 'Tipo de pantalla'),
            'usb_ports':         ('connection', 'USB'),
            'vesa':              ('dimensions', 'Medidas VESA'),
            'weight':            ('dimensions', 'Peso'),
            'width':             ('dimensions', 'Ancho'),
            'width_b':           ('dimensions', 'Ancho \(con base\)'),
            'youtube':           ('extras', 'YouTube'),
        }

        parse_map = {
            'current_price':     number_stripper,
            'previous_price':    number_stripper,
            'inches':            number_stripper,
            'height':            number_stripper,
            'height_b':          number_stripper,
            'depth':             number_stripper,
            'depth_b':           number_stripper,
            'width':             number_stripper,
            'width_b':           number_stripper,
            'weight':            number_stripper,
            'usb_ports':         number_stripper,
            'hdmi_ports':        number_stripper,
            'youtube':           yes_no_parser,
            'wifi':              yes_no_parser,
            'netflix':           yes_no_parser,
            'resolution':        reslution_parser,
            'vesa':              reslution_parser,
        }

        def r(x, y):
            p = re.compile(y, flags=re.I)
            get_key = list(filter(lambda m: m, map(lambda s: p.match(s), x.keys())))
            keys = [i.string for i in get_key if len(i.string) == len(i.group())]
            first_key = keys[0] if keys else None
            return x.get(first_key, {})

        for att, path in attr_map.items():
            value = reduce(r, path, garba)
            if isinstance(value, dict) and not value:
                value = None
            if value is not None:
                parser = parse_map.get(att, lambda x: x)
                attrs[att] = parser(value)
            else:
                attrs[att] = value

        return cls(**attrs)


def number_stripper(s):
    decimal_set = string.digits + ","
    sp = "".join([c for c in s if c in decimal_set])
    sp = sp.replace(",", ".") # setting to SI
    try:
        return Decimal(sp)
    except:
        return None


def yes_no_parser(s):
    """docstring for yes_no_parser"""
    p_yes = re.compile('s[i-í]', re.I)
    p_no = re.compile('no', re.I)
    try:
        if p_yes.match(s):
            return True
        elif p_no.match(s):
            return False
    except:
        return None


def reslution_parser(s):
    """docstring for reslution_parser"""
    sp = s.strip().replace(" ","")
    p = re.compile('\d*x\d*')
    m = p.match(sp)
    if m:
        return m.group()
    return s


