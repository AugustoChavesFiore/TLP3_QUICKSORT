def quicksort(list):
    #Verificar si la lista tiene 0 o 1 elementos
    if len(list) <= 1:
        return list
    else:
        #Seleccionar el pivote
        pivot = list[0]
        #Partición de la lista
        less =[]
        greater = []
        equal = []
        #Recorrer la lista
        for i in list:
            #Reorganizar los elementos de la sublista
            #Menores que el pivote
            if i < pivot:
                less.append(i)
                #Iguales al pivote
            elif i == pivot:
                equal.append(i)
                #Mayores que el pivote
            else:
                greater.append(i)
    #Llamadas recursivas y concatenación de las sublistas
        return quicksort(less) + equal + quicksort(greater)


# Pruebas
assert(quicksort([3,6,8,10,1,2,1]) == [1,1,2,3,6,8,10])
assert(quicksort([1, 0, 0, 1]) == [0, 0, 1, 1])
assert(quicksort([3, 3, 3, 3]) == [3, 3, 3, 3])
assert(quicksort([4, 3, 2, 1]) == [1, 2, 3, 4])

if __name__ == "__main__":
    print("Pruebas exitosas")

