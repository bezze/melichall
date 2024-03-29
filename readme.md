Dividi el proceso en 5 etapas. Las primeras 4 son simetricas, y consiste en
primero descargar los links del catalogo de televisores de fravega y garbarino.

```python3 frave-scrap/get_product_urls.py```

```python3 garba-scrap/get_product_urls.py```

Luego procedo a examinar cada uno de esos links y parseo la informacion cruda en
estructuras afines al formato de cada pagina.

```python3 frave-scrap/process_item.py```

```python3 garba-scrap/process_item.py```


Por ultimo, corro el script que parsea las estructuras y las traduce a un objeto
idealizado, que comparte caracteristicas de ambas. La idea es poder comparar
estos objetos.

```python3 main.py```

La heuristica que utilice es muy sencilla, y basicamente toma el
numero de coincidencias entre los atributos de dos objetos distintos como
"norma" para establecer la distancia entre ellos.

Agrupo los resultados en una matriz, donde cada columna son items de garbarino y
cada fila son items de fravega. La interseccion es el valor de esta norma.

```
================================================================================
    00         01         02         03         04         05         06         07         08         09         10         11         12         13         14  
00 [0.29 0.17, 0.14 0.08, 0.07 0.04, 0.36 0.21, 0.29 0.17, 0.07 0.04, 0.21 0.12, 0.07 0.04, 0.21 0.12, 0.07 0.04, 0.29 0.17, 0.00 0.00, 0.21 0.12, 0.00 0.00, 0.00 0.00]
01 [0.40 0.17, 0.20 0.08, 0.10 0.04, 0.50 0.21, 0.40 0.17, 0.10 0.04, 0.20 0.08, 0.10 0.04, 0.40 0.17, 0.10 0.04, 0.40 0.17, 0.00 0.00, 0.20 0.08, 0.00 0.00, 0.00 0.00]
02 [0.10 0.04, 0.40 0.17, 0.00 0.00, 0.20 0.08, 0.10 0.04, 0.00 0.00, 0.50 0.21, 0.10 0.04, 0.10 0.04, 0.00 0.00, 0.20 0.08, 0.00 0.00, 0.50 0.21, 0.00 0.00, 0.00 0.00]
03 [0.31 0.17, 0.15 0.08, 0.08 0.04, 0.38 0.21, 0.31 0.17, 0.08 0.04, 0.23 0.12, 0.08 0.04, 0.23 0.12, 0.08 0.04, 0.31 0.17, 0.00 0.00, 0.23 0.12, 0.00 0.00, 0.00 0.00]
04 [0.08 0.04, 0.08 0.04, 0.31 0.17, 0.00 0.00, 0.08 0.04, 0.31 0.17, 0.00 0.00, 0.15 0.08, 0.15 0.08, 0.23 0.12, 0.08 0.04, 0.23 0.12, 0.00 0.00, 0.15 0.08, 0.15 0.08]
05 [0.20 0.08, 0.20 0.08, 0.20 0.08, 0.10 0.04, 0.20 0.08, 0.20 0.08, 0.10 0.04, 0.30 0.12, 0.20 0.08, 0.20 0.08, 0.20 0.08, 0.10 0.04, 0.10 0.04, 0.20 0.08, 0.20 0.08]
06 [0.11 0.04, 0.33 0.12, 0.33 0.12, 0.11 0.04, 0.11 0.04, 0.22 0.08, 0.11 0.04, 0.56 0.21, 0.22 0.08, 0.22 0.08, 0.11 0.04, 0.22 0.08, 0.22 0.08, 0.33 0.12, 0.33 0.12]
07 [0.56 0.21, 0.22 0.08, 0.11 0.04, 0.44 0.17, 0.67 0.25, 0.11 0.04, 0.11 0.04, 0.11 0.04, 0.44 0.17, 0.11 0.04, 0.67 0.25, 0.11 0.04, 0.11 0.04, 0.11 0.04, 0.11 0.04]
08 [0.22 0.08, 0.67 0.25, 0.22 0.08, 0.44 0.17, 0.22 0.08, 0.11 0.04, 0.67 0.25, 0.33 0.12, 0.22 0.08, 0.11 0.04, 0.22 0.08, 0.00 0.00, 0.78 0.29, 0.00 0.00, 0.00 0.00]
09 [0.08 0.04, 0.17 0.08, 0.33 0.17, 0.08 0.04, 0.08 0.04, 0.25 0.12, 0.00 0.00, 0.25 0.12, 0.25 0.12, 0.33 0.17, 0.08 0.04, 0.33 0.17, 0.08 0.04, 0.25 0.12, 0.25 0.12]
10 [0.00 0.00, 0.00 0.00, 0.22 0.08, 0.00 0.00, 0.00 0.00, 0.22 0.08, 0.00 0.00, 0.11 0.04, 0.11 0.04, 0.44 0.17, 0.00 0.00, 0.33 0.12, 0.00 0.00, 0.22 0.08, 0.22 0.08]
11 [0.10 0.04, 0.10 0.04, 0.30 0.12, 0.00 0.00, 0.10 0.04, 0.30 0.12, 0.00 0.00, 0.20 0.08, 0.20 0.08, 0.40 0.17, 0.10 0.04, 0.50 0.21, 0.00 0.00, 0.30 0.12, 0.40 0.17]
12 [0.00 0.00, 0.00 0.00, 0.22 0.08, 0.00 0.00, 0.00 0.00, 0.22 0.08, 0.00 0.00, 0.11 0.04, 0.11 0.04, 0.33 0.12, 0.00 0.00, 0.22 0.08, 0.00 0.00, 0.11 0.04, 0.11 0.04]
13 [0.00 0.00, 0.00 0.00, 0.10 0.04, 0.00 0.00, 0.00 0.00, 0.10 0.04, 0.00 0.00, 0.20 0.08, 0.00 0.00, 0.10 0.04, 0.00 0.00, 0.20 0.08, 0.00 0.00, 0.20 0.08, 0.30 0.12]
14 [0.00 0.00, 0.00 0.00, 0.10 0.04, 0.00 0.00, 0.00 0.00, 0.10 0.04, 0.00 0.00, 0.20 0.08, 0.00 0.00, 0.20 0.08, 0.00 0.00, 0.30 0.12, 0.00 0.00, 0.30 0.12, 0.40 0.17]
15 [0.22 0.08, 0.44 0.17, 0.11 0.04, 0.11 0.04, 0.22 0.08, 0.11 0.04, 0.33 0.12, 0.11 0.04, 0.11 0.04, 0.11 0.04, 0.22 0.08, 0.11 0.04, 0.33 0.12, 0.11 0.04, 0.11 0.04]
16 [0.00 0.00, 0.00 0.00, 0.10 0.04, 0.00 0.00, 0.00 0.00, 0.10 0.04, 0.00 0.00, 0.20 0.08, 0.00 0.00, 0.10 0.04, 0.00 0.00, 0.10 0.04, 0.00 0.00, 0.30 0.12, 0.20 0.08]
17 [0.10 0.04, 0.10 0.04, 0.40 0.17, 0.10 0.04, 0.10 0.04, 0.40 0.17, 0.10 0.04, 0.20 0.08, 0.20 0.08, 0.30 0.12, 0.10 0.04, 0.20 0.08, 0.10 0.04, 0.10 0.04, 0.10 0.04]
18 [0.20 0.08, 0.20 0.08, 0.40 0.17, 0.10 0.04, 0.20 0.08, 0.40 0.17, 0.10 0.04, 0.30 0.12, 0.30 0.12, 0.60 0.25, 0.20 0.08, 0.40 0.17, 0.10 0.04, 0.30 0.12, 0.30 0.12]
19 [0.10 0.04, 0.10 0.04, 0.30 0.12, 0.10 0.04, 0.10 0.04, 0.30 0.12, 0.10 0.04, 0.20 0.08, 0.20 0.08, 0.30 0.12, 0.10 0.04, 0.20 0.08, 0.10 0.04, 0.10 0.04, 0.10 0.04]
20 [0.00 0.00, 0.00 0.00, 0.05 0.04, 0.00 0.00, 0.00 0.00, 0.05 0.04, 0.00 0.00, 0.05 0.04, 0.00 0.00, 0.05 0.04, 0.00 0.00, 0.05 0.04, 0.00 0.00, 0.05 0.04, 0.05 0.04]
21 [0.22 0.08, 0.44 0.17, 0.44 0.17, 0.22 0.08, 0.22 0.08, 0.33 0.12, 0.22 0.08, 0.33 0.12, 0.44 0.17, 0.33 0.12, 0.22 0.08, 0.22 0.08, 0.33 0.12, 0.11 0.04, 0.11 0.04]
22 [0.00 0.00, 0.00 0.00, 0.05 0.04, 0.00 0.00, 0.00 0.00, 0.05 0.04, 0.00 0.00, 0.05 0.04, 0.00 0.00, 0.11 0.08, 0.00 0.00, 0.11 0.08, 0.00 0.00, 0.11 0.08, 0.11 0.08]
23 [0.05 0.04, 0.16 0.12, 0.05 0.04, 0.05 0.04, 0.05 0.04, 0.05 0.04, 0.16 0.12, 0.05 0.04, 0.05 0.04, 0.05 0.04, 0.05 0.04, 0.00 0.00, 0.16 0.12, 0.00 0.00, 0.00 0.00]
24 [0.05 0.04, 0.16 0.12, 0.05 0.04, 0.05 0.04, 0.05 0.04, 0.05 0.04, 0.16 0.12, 0.05 0.04, 0.05 0.04, 0.05 0.04, 0.05 0.04, 0.00 0.00, 0.16 0.12, 0.00 0.00, 0.00 0.00]
25 [0.21 0.17, 0.05 0.04, 0.05 0.04, 0.21 0.17, 0.21 0.17, 0.05 0.04, 0.05 0.04, 0.05 0.04, 0.21 0.17, 0.05 0.04, 0.21 0.17, 0.00 0.00, 0.05 0.04, 0.00 0.00, 0.00 0.00]
26 [0.15 0.08, 0.38 0.21, 0.23 0.12, 0.08 0.04, 0.15 0.08, 0.23 0.12, 0.31 0.17, 0.23 0.12, 0.23 0.12, 0.23 0.12, 0.15 0.08, 0.15 0.08, 0.31 0.17, 0.08 0.04, 0.08 0.04]
================================================================================
(0.5555555555555556, 0.20833333333333334)
Item(aspect=None, current_price=29999, depth=8.67, depth_b=25.82, hdmi_ports=4, height=56.24, height_b=62.82, inches=43, internet=None, model=43PUG6102/77, name=Smart TV 4K 43" Philips 43PUG6102/77, netflix=True, previous_price=33999, refresh=None, res_type=4K UHD, resolution=3840x2160, screen_format=Plano, screen_type=LED 4K Ultra HD, tv_type=None, usb_ports=2, vesa=200x200, vga_ports=None, weight=9.2, width=96.8, width_b=96.8, wifi=None, youtube=None)
Item(aspect=None, current_price=29999, depth=86, depth_b=258, hdmi_ports=4, height=562, height_b=628, inches=43, internet=None, model=None, name=Smart TV Philips 43 " 4K Ultra HD 43PUG6102/77, netflix=None, previous_price=33999, refresh=None, res_type=4K Ultra HD, resolution=3840x2160, screen_format=Plana, screen_type=LED, tv_type=None, usb_ports=2, vesa=200x200, vga_ports=None, weight=89, width=968, width_b=968, wifi=None, youtube=None)
----------
(0.6666666666666666, 0.25)
Item(aspect=None, current_price=15999, depth=7.73, depth_b=17.93, hdmi_ports=2, height=43.53, height_b=49.41, inches=32, internet=None, model=PHG5813/77, name=Smart TV 32" HD Philips 32PHG5813/77, netflix=True, previous_price=16999, refresh=None, res_type=HD, resolution=1366x768, screen_format=Plano, screen_type=LED HD, tv_type=None, usb_ports=2, vesa=100x100, vga_ports=None, weight=4.6, width=73.18, width_b=73.18, wifi=None, youtube=None)
Item(aspect=None, current_price=15999, depth=773, depth_b=1793, hdmi_ports=2, height=4353, height_b=4941, inches=32, internet=None, model=None, name=Smart TV Philips 32 " HD 32PHG5813/77, netflix=None, previous_price=18499, refresh=None, res_type=HD, resolution=1366x768, screen_format=Plana, screen_type=LED, tv_type=None, usb_ports=2, vesa=100x100, vga_ports=None, weight=46, width=7353, width_b=7318, wifi=None, youtube=None)
----------
```
