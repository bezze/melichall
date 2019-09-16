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
