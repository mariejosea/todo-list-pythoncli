#Lectura y escritura de archivos csv (modulo de documentación) 
#para guardar y salvar las tareas.
import csv

todos = []
stop = False
 
def get_todos():
    global todos
    return todos

def add_one_task(title):
    """ 
        This function: agrega una tarea a la lista todos (utilizando append) 
        e informa que ha sido agregada.
    """
    global todos
    todos.append(title)
    print("\nLa tarea ha sido agregada")

def print_list():
    """ 
        This function: imprime la lista de tareas que han sido agregadas, 
        indicando la posición de cada una.
    """
    global todos
    print("\nLista de tareas:")
    count = 1
    for todo in todos:
        print(str(count)+'. '+(todos[count-1]))
        count = count + 1
    print(f"\nTotal de tareas = {str(len(todos))}") 

def delete_task(number_to_delete):
    """
        This function: elimina un elemento de la lista ingresando la posición de la tarea
        e imprime el número de la tarea que fue eliminada.
    """
    global todos
    #el índice de la tarea eliminada muestra en vez de 1, el 0
    #new_todos = []
    #number_to_delete = int(number_to_delete)- 1
    #for i in range (0, len(todos)):
        #if i != number_to_delete:
            #new_todos.append(todos[i])
    #todos = new_todos

    todos.pop(int(number_to_delete)- 1)
    print(f"\nLa tarea {number_to_delete} fue eliminada.")

def save_todos():
    """
        This function: guarda las tarea en un archivo csv creado (todos.csv).
    """
    global todos
    #open devuelve un objeto archivo 
    with open('todos.csv', 'w', newline='') as file:
        #se crea un objeto de escritura en el archivo (file), y el parametro 
        # delimitador especifica un espacio de línea en los datos.
        f_writer = csv.writer(file, delimiter="\n")
        #writerow escribe un elemento en cada fila del archivo. En este caso la lista todos.
        f_writer.writerow(todos)
        #cierre del archivo f_writer
        file.close()
    print("La tarea ha sido guardada en el archivo: todos.csv")
    
def load_todos():
    """
        This function: carga (actualiza) la lista de tareas según el archivo todos.csv. 
    """
    global todos
    #no se especifica la (r) porque por defecto es de lectura. 
    with open('todos.csv', newline='') as file:
        f_reader = csv.reader(file, delimiter="\n")
        #clear borrar la lista que estaba guardada en el archivo todos.csv, y actualiza las tareas
        #que fueorn borradas o agregadas. 
        todos.clear()
        #la data que que tiene el archivo f_reader, será separada en filas.
        for row in f_reader:
            print(' ***** ' .join(row))
            todos.append(*row)
            #el (*) se utiliza para que no se escriban los elementos con '' y []. 


# Below this code will only run if the entry file running was app.py
if __name__ == '__main__':
    while stop == False:
        print("""
    Choose an option: 
        1. Add one task
        2. Delete a task
        3. Print the current list of tasks
        4. Save todo's to todos.csv
        5. Load todo's from todos.csv
        6. Exit
    """)
        response = input()
        if response == "6":
            stop = True
            print("See you soon!")
        elif response == "3":
            print_list()
        elif response == "2":
            print("What task number you want to delete?")
            number_to_delete = input()
            delete_task(number_to_delete)
        elif response == "1":
            print("What is your task title?")
            title = input()
            add_one_task(title)
        elif response == "4":
            print("Saving todo's...")
            save_todos()
        elif response == "5":
            print("Loading todo's...")
            load_todos()
        else:
            print("Invalid response, asking again...")