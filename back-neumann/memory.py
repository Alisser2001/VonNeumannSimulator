def memory(tableOfMemory, direction, operation=None, value=None):
    if operation is None: return tableOfMemory[direction]
    if operation=="0110": 
        tableOfMemory[direction] = value
        return 
    if operation=="0000":
        return tableOfMemory[direction]

