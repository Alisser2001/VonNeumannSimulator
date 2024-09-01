from fastapi import FastAPI
from memory import memory
from alu import ALU

app = FastAPI()

tableOfMemory = {
        "0000": "01100110",
        "0001": "01100111",
        "0010": "00000110",
        "0011": "00000111",
        "0100": "01101000",
        "0101": "01110000",
        "0110": "00000000",
        "0111": "00000000",
        "1000": "00000000"
    }

@app.get('/')
def read_root(x, y):
    instructions = []
    if len(to_binary8((int(x)+int(y))))>8:
        return ("No se puede sumar")
    bin_x = to_binary8(int(x))
    bin_y = to_binary8(int(y))
    acc = to_binary8(0)
    cont = 0
    instructions.append({
            "component": "Control Unit",
            "subcomponent": "Counter",
            "description": "Se inicializa el contador del programa en 0.",
            "changes": {
                "Counter": to_binary4(cont)
            }
        })
    operation = None



    while operation != "0111":
        r_data = memory(tableOfMemory, to_binary4(cont))
        instructions.append({
            "component": "Memory",
            "subcomponent": "R. Directions",
            "description": "La Unidad de control envía una micro-orden para transferir el contenido del Contador de programa al Registro de direcciones.",
            "changes": {
                "R. Directions": to_binary4(cont)
            }
        })
        cont += 1


        instructions.append({
            "component": "Control Unit",
            "subcomponent": "Counter",
            "description": "El Contador de programa aumenta en uno, por lo que su contenido será la dirección de la próxima instrucción a ejecutar.",
            "changes": {
                "Counter": to_binary4(cont)
            }
        })
        instructions.append({
            "component": "Memory",
            "subcomponent": "Table of Memory",
            "description": "Se selecciona la posición de memoria que indica el Registro de direcciones y se realiza una lectura en la memoria.",
            "changes": {
                "Table of Memory": r_data
            }
        })
        instructions.append({
            "component": "Memory",
            "subcomponent": "R. Data",
            "description": "Se deposita en el Registro de datos la instrucción a ejecutar.",
            "changes": {
                "R. Data": r_data
            }
        })
        instructions.append({
            "component": "Control Unit",
            "subcomponent": "R. Instructions",
            "description": "Se realiza el traslado de la información contenida en el Registro de datos al Registro de instrucciones, donde se almacenará.",
            "changes": {
                "R. Intructions": r_data
            }
        })


        operation = decoOP(r_data)
        position = decoPO(r_data)
        instructions.append({
            "component": "Control Unit",
            "subcomponent": "Decoder",
            "description": "El Decodificador procede a la interpretación de la instrucción que serán los 4 primeros bits, es decir, interpreta el código de operación.",
            "changes": {
                "Decoder": operation
            }
        })


        if operation=="0110" and position=="0110":
            memory(tableOfMemory, position, operation=operation, value=bin_x)
            instructions.append({
            "component": "Memory",
            "subcomponent": "R. Directions",
            "description": "El Registro de instrucciones envía los 4 últimos bits al Registro de direcciones.",
            "changes": {
                "R. Directions": position
            }
        })
            instructions.append({
            "component": "Memory",
            "subcomponent": "Table of Memory",
            "description": "El Registro de instrucciones le indica a la Tabla de memoria en que posicion guardar el nuevo dato y lo almacena",
            "changes": {
                "Table of Memory": bin_x
            }
        })
            

        if operation=="0110" and position=="0111":
            memory(tableOfMemory, position, operation=operation, value=bin_y)
            instructions.append({
            "component": "Memory",
            "subcomponent": "R. Directions",
            "description": "El Registro de instrucciones envía los 4 últimos bits al Registro de direcciones.",
            "changes": {
                "R. Directions": position
            }
        })
            instructions.append({
            "component": "Memory",
            "subcomponent": "Table of Memory",
            "description": "El Registro de instrucciones le indica a la Tabla de memoria en que posicion guardar el nuevo dato y lo almacena",
            "changes": {
                "Table of Memory": bin_y
            }
        })
            

        if operation=="0000":
            value = memory(tableOfMemory, position, operation=operation)
            instructions.append({
            "component": "Memory",
            "subcomponent": "R. Directions",
            "description": "El Registro de instrucciones envía los 4 últimos bits al Registro de direcciones.",
            "changes": {
                "R. Directions": position
            }
        })
            instructions.append({
            "component": "Memory",
            "subcomponent": "Table of Memory",
            "description": "Se selecciona la posición de memoria que indica el Registro de direcciones y se realiza una lectura en la memoria.",
            "changes": {
                "Table of Memory": r_data
            }
        })
            instructions.append({
            "component": "Memory",
            "subcomponent": "R. Data",
            "description": "La información es enviada al Registro de datos.",
            "changes": {
                "R. Data": value
            }
        })
            instructions.append({
            "component": "ALU",
            "subcomponent": "R. Entry",
            "description": "El Registro de datos envía la información al Registro de entrada.",
            "changes": {
                "R. Entry": value
            }
        })
            acc = ALU(acc, value)
            instructions.append({
            "component": "ALU",
            "subcomponent": "Acumulator",
            "description": "El Circuito operacional realiza la operación con el Registro acumulador y el Registro de entrada y lo almacena de nuevo en el Registro acumulador.",
            "changes": {
                "Acumulator": acc
            }
        })


        if operation=="0110" and position=="1000":
            memory(tableOfMemory, position, operation=operation, value=acc)
            instructions.append({
            "component": "Memory",
            "subcomponent": "R. Directions",
            "description": "El Registro de instrucciones envía los 4 últimos bits al Registro de direcciones.",
            "changes": {
                "R. Directions": position
            }
        })
            instructions.append({
            "component": "Memory",
            "subcomponent": "Table of Memory",
            "description": "El Registro de direcciones busca en la memoria la celda en la que será almacenada el resultado.",
            "changes": {
                "Table of Memory": "00000000"
            }
        })
            instructions.append({
            "component": "Memory",
            "subcomponent": "R. Data",
            "description": "El Registro acumulador envía la información al Registro de datos.",
            "changes": {
                "R. Data": acc
            }
        })
            instructions.append({
            "component": "Memory",
            "subcomponent": "Table of Memory",
            "description": "El Registro de datos procede a la escritura de la información en la celda seleccionada por el Registro de Direcciones.",
            "changes": {
                "Table of Memory": acc
            }
        })
            

        if operation=="0111":
            instructions.append({
            "component": "Control Unit",
            "subcomponent": "Decode",
            "description": "El decodificador intepreta que se finaliza el programa y se para la ejecución",
            "changes": {
                "Decode": operation
            }
        })
            return instructions

def decoOP(binary):
    return binary[:4]

def decoPO(binary):
    return binary[4:]

def to_binary4(value):
    return format(value, '04b')

def to_binary8(value):
    return format(value, '08b')