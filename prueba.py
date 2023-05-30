def buscar_por_clave(lista: list, key: str, patron: str)->dict:

    if isinstance(lista, list) and lista and all(isinstance(dicc, dict) and dicc and isinstance(key, str) and key and key in dicc for dicc in lista):
        print("pase")
        
    else:
        print("no pase")


lista = [{"nombre":"juan"}]

buscar_por_clave(lista, "marca", "asd")