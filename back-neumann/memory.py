def memory(tableOfMemory, r_dir, operation=None, value=None):
    if operation is None: return tableOfMemory[r_dir]
    if operation=="0110" and value is not None: 
        tableOfMemory[r_dir] = value
        return 
    if operation=="0000":
        return tableOfMemory[r_dir]

