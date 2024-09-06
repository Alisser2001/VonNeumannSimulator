from fastapi import FastAPI
from memory import memory
from alu import ALU
from fastapi.middleware.cors import CORSMiddleware
import copy

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins="http://localhost:3000",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
def read_root(x, y):
    instructions = []
    if len(to_binary8((int(x)+int(y))))>8:
        return ("No se puede sumar")
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
    bin_x = to_binary8(int(x))
    bin_y = to_binary8(int(y))
    operation = "0000"
    cont = 0
    acc = "00000000"
    instructions.append({
            "description": "Se inicializa el contador del programa en 0.",
            "state": {
                "counter": to_binary4(cont),
                "decoder": operation,
                "r_instructions": "00000000",
                "r_directions": "0000",
                "table_of_memory": copy.deepcopy(tableOfMemory),
                "r_data": "00000000",
                "r_entry": "00000000",
                "accumulator": acc

            }
        })

    while operation != "0111":
        r_data = memory(tableOfMemory, to_binary4(cont))
        instructions.append({
            "description": "La Unidad de control envía una micro-orden para transferir el contenido del Contador de programa al Registro de direcciones.",
            "state": {
                "counter": to_binary4(cont),
                "decoder": operation,
                "r_instructions": "00000000",
                "r_directions": "0000",
                "table_of_memory": copy.deepcopy(tableOfMemory),
                "r_data": "00000000",
                "r_entry": "00000000",
                "accumulator": acc

            }
        })
        cont += 1


        instructions.append({
            "description": "El Contador de programa aumenta en uno, por lo que su contenido será la dirección de la próxima instrucción a ejecutar.",
            "state": {
                "counter": to_binary4(cont),
                "decoder": operation,
                "r_instructions": "00000000",
                "r_directions": "0000",
                "table_of_memory": copy.deepcopy(tableOfMemory),
                "r_data": "00000000",
                "r_entry": "00000000",
                "accumulator": acc

            }
        })
        instructions.append({
            "description": "Se selecciona la posición de memoria que indica el Registro de direcciones y se realiza una lectura en la memoria.",
            "state": {
                "counter": to_binary4(cont),
                "decoder": operation,
                "r_instructions": "00000000",
                "r_directions": "0000",
                "table_of_memory": copy.deepcopy(tableOfMemory),
                "r_data": "00000000",
                "r_entry": "00000000",
                "accumulator": acc

            }
        })
        instructions.append({
            "description": "Se deposita en el Registro de datos la instrucción a ejecutar.",
            "state": {
                "counter": to_binary4(cont),
                "decoder": operation,
                "r_instructions": "00000000",
                "r_directions": "0000",
                "table_of_memory": copy.deepcopy(tableOfMemory),
                "r_data": "00000000",
                "r_entry": "00000000",
                "accumulator": acc

            }
        })
        instructions.append({
            "description": "Se realiza el traslado de la información contenida en el Registro de datos al Registro de instrucciones, donde se almacenará.",
            "state": {
                "counter": to_binary4(cont),
                "decoder": operation,
                "r_instructions": "00000000",
                "r_directions": "0000",
                "table_of_memory": copy.deepcopy(tableOfMemory),
                "r_data": "00000000",
                "r_entry": "00000000",
                "accumulator": acc

            }
        })


        operation = decoOP(r_data)
        position = decoPO(r_data)
        instructions.append({
            "description": "El Decodificador procede a la interpretación de la instrucción que serán los 4 primeros bits, es decir, interpreta el código de operación.",
            "state": {
                "counter": to_binary4(cont),
                "decoder": operation,
                "r_instructions": "00000000",
                "r_directions": "0000",
                "table_of_memory": copy.deepcopy(tableOfMemory),
                "r_data": "00000000",
                "r_entry": "00000000",
                "accumulator": acc

            }
        })


        if operation=="0110" and position=="0110":
            memory(tableOfMemory, position, operation=operation, value=bin_x)
            instructions.append({
            "description": "El Registro de instrucciones envía los 4 últimos bits al Registro de direcciones.",
            "state": {
                "counter": to_binary4(cont),
                "decoder": operation,
                "r_instructions": "00000000",
                "r_directions": "0000",
                "table_of_memory": copy.deepcopy(tableOfMemory),
                "r_data": "00000000",
                "r_entry": "00000000",
                "accumulator": acc

            }
        })
            instructions.append({
            "description": "El Registro de instrucciones le indica a la Tabla de memoria en que posicion guardar el nuevo dato y lo almacena",
            "state": {
                "counter": to_binary4(cont),
                "decoder": operation,
                "r_instructions": "00000000",
                "r_directions": "0000",
                "table_of_memory": copy.deepcopy(tableOfMemory),
                "r_data": "00000000",
                "r_entry": "00000000",
                "accumulator": acc

            }
        })
            

        if operation=="0110" and position=="0111":
            memory(tableOfMemory, position, operation=operation, value=bin_y)
            instructions.append({
            "description": "El Registro de instrucciones envía los 4 últimos bits al Registro de direcciones.",
            "state": {
                "counter": to_binary4(cont),
                "decoder": operation,
                "r_instructions": "00000000",
                "r_directions": "0000",
                "table_of_memory": copy.deepcopy(tableOfMemory),
                "r_data": "00000000",
                "r_entry": "00000000",
                "accumulator": acc

            }
        })
            instructions.append({
            "description": "El Registro de instrucciones le indica a la Tabla de memoria en que posicion guardar el nuevo dato y lo almacena",
            "state": {
                "counter": to_binary4(cont),
                "decoder": operation,
                "r_instructions": "00000000",
                "r_directions": "0000",
                "table_of_memory": copy.deepcopy(tableOfMemory),
                "r_data": "00000000",
                "r_entry": "00000000",
                "accumulator": acc

            }
        })
            

        if operation=="0000":
            value = memory(tableOfMemory, position, operation=operation)
            instructions.append({
            "description": "El Registro de instrucciones envía los 4 últimos bits al Registro de direcciones.",
            "state": {
                "counter": to_binary4(cont),
                "decoder": operation,
                "r_instructions": "00000000",
                "r_directions": "0000",
                "table_of_memory": copy.deepcopy(tableOfMemory),
                "r_data": "00000000",
                "r_entry": "00000000",
                "accumulator": acc

            }
        })
            instructions.append({
            "description": "Se selecciona la posición de memoria que indica el Registro de direcciones y se realiza una lectura en la memoria.",
            "state": {
                "counter": to_binary4(cont),
                "decoder": operation,
                "r_instructions": "00000000",
                "r_directions": "0000",
                "table_of_memory": copy.deepcopy(tableOfMemory),
                "r_data": "00000000",
                "r_entry": "00000000",
                "accumulator": acc

            }
        })
            instructions.append({
            "description": "La información es enviada al Registro de datos.",
            "state": {
                "counter": to_binary4(cont),
                "decoder": operation,
                "r_instructions": "00000000",
                "r_directions": "0000",
                "table_of_memory": copy.deepcopy(tableOfMemory),
                "r_data": "00000000",
                "r_entry": "00000000",
                "accumulator": acc

            }
        })
            instructions.append({
            "description": "El Registro de datos envía la información al Registro de entrada.",
            "state": {
                "counter": to_binary4(cont),
                "decoder": operation,
                "r_instructions": "00000000",
                "r_directions": "0000",
                "table_of_memory": copy.deepcopy(tableOfMemory),
                "r_data": "00000000",
                "r_entry": "00000000",
                "accumulator": acc

            }
        })
            acc = ALU(acc, value)
            instructions.append({
            "description": "El Circuito operacional realiza la operación con el Registro acumulador y el Registro de entrada y lo almacena de nuevo en el Registro acumulador.",
            "state": {
                "counter": to_binary4(cont),
                "decoder": operation,
                "r_instructions": "00000000",
                "r_directions": "0000",
                "table_of_memory": copy.deepcopy(tableOfMemory),
                "r_data": "00000000",
                "r_entry": "00000000",
                "accumulator": acc

            }
        })


        if operation=="0110" and position=="1000":
            memory(tableOfMemory, position, operation=operation, value=acc)
            instructions.append({
            "description": "El Registro de instrucciones envía los 4 últimos bits al Registro de direcciones.",
            "state": {
                "counter": to_binary4(cont),
                "decoder": operation,
                "r_instructions": "00000000",
                "r_directions": "0000",
                "table_of_memory": copy.deepcopy(tableOfMemory),
                "r_data": "00000000",
                "r_entry": "00000000",
                "accumulator": acc

            }
        })
            instructions.append({
            "description": "El Registro de direcciones busca en la memoria la celda en la que será almacenada el resultado.",
            "state": {
                "counter": to_binary4(cont),
                "decoder": operation,
                "r_instructions": "00000000",
                "r_directions": "0000",
                "table_of_memory": copy.deepcopy(tableOfMemory),
                "r_data": "00000000",
                "r_entry": "00000000",
                "accumulator": acc

            }
        })
            instructions.append({
            "description": "El Registro acumulador envía la información al Registro de datos.",
            "state": {
                "counter": to_binary4(cont),
                "decoder": operation,
                "r_instructions": "00000000",
                "r_directions": "0000",
                "table_of_memory": copy.deepcopy(tableOfMemory),
                "r_data": "00000000",
                "r_entry": "00000000",
                "accumulator": acc

            }
        })
            instructions.append({
            "description": "El Registro de datos procede a la escritura de la información en la celda seleccionada por el Registro de Direcciones.",
            "state": {
                "counter": to_binary4(cont),
                "decoder": operation,
                "r_instructions": "00000000",
                "r_directions": "0000",
                "table_of_memory": copy.deepcopy(tableOfMemory),
                "r_data": "00000000",
                "r_entry": "00000000",
                "accumulator": acc

            }
        })
            

        if operation=="0111":
            instructions.append({
            "description": "El decodificador intepreta que se finaliza el programa y se para la ejecución",
            "state": {
                "counter": to_binary4(cont),
                "decoder": operation,
                "r_instructions": "00000000",
                "r_directions": "0000",
                "table_of_memory": copy.deepcopy(tableOfMemory),
                "r_data": "00000000",
                "r_entry": "00000000",
                "accumulator": acc

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