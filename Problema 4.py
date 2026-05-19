### Matriz 
matrizvideoteca = [
    ["El Padrino", 1972, 8.8, "Accion"],
    ["El Señor de los Anillos", 2001, 8.8, "Aventura"],
    ["Titanic", 1997, 7.8, "Drama"],
    ["Inception", 2010, 8.8, "Ciencia Ficción"],
    ["Matrix", 1999, 8.7, "Ciencia Ficción"],
    ["El Club de la Pelea", 1999, 8.8, "Drama"],
    ["Parasite", 2019, 8.6, "Drama"]
]

def contar_titulos(matriz, califi, ano):
    count = 0
    for pelicula in matriz:

        ano_lanzamiento = pelicula[1]
        calificacion = pelicula[2]


        if calificacion >= califi and ano_lanzamiento >= ano:
            count += 1
            
    return count

def main():
    # Parámetros numéricos correctos
    califi = 8.0
    ano = 1999
    
    print("===============================================================================")
    print("                              AUDITORIA DE VIDEOTECA                           ")
    print("===============================================================================")
    print(f"-> Parámetros de búsqueda establecidos:")
    print(f"   * Calificación mínima: {califi}")
    print(f"   * Año de lanzamiento: {ano}")
    

    resultado = contar_titulos(matrizvideoteca, califi, ano)

    print("===============================================================================")
    print(f"El número de títulos con calificación mayor o igual a {califi}")
    print(f"y lanzados en el año {ano} o posterior es: {resultado}")
    print("===============================================================================")

if __name__ == "__main__":
    main()