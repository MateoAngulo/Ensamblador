'''Toma un string como entrada y elimina cualquier carácter de salto de línea'''
'''Elimina cualquier carácter de salto de línea ("\n") de una cadena.'''
def takeJumpAway(string): 
    newString=string.replace("\n","") # Reemplaza los saltos de línea por una cadena vacía
    return newString
'''En un vector'''
'''Elimina saltos de línea en cada cadena dentro de una lista.'''
def takeJumpAwayArray(list):
    l1=[] # Nueva lista para almacenar las cadenas sin saltos de línea
    count=0
    tam=len(list)
    for word in list:
        count+=1
        if (count == tam): # Si es el último elemento de la lista, se le quitan los saltos de línea
            l1.append(takeJumpAway(word))
        else:
            l1.append(word) # Se agrega tal cual si no es el último
    return l1

'''Encuentra el tipo de instrucción en un diccionario según el valor asociado.'''
def find_the_type(dictionary,word):
    type=""
    for new_k,new_val in dictionary.items():
        for i in new_val:
            if word==i:
                type=new_k # Si encuentra la palabra en el valor del diccionario, guarda la clave correspondiente (el tipo)

                break
    return type

'''Decodifica identificadores específicos para valores de registro.'''
def decode_identifier(string):
    if string=='ra':
        return 1
    elif string=='sp':
        return 2
    else:
        return int(string.replace("x","")) # Remueve la 'x' y convierte el número a entero
    
'''Genera una instrucción de tipo R en formato binario.'''
'''agregar un elemento al final de una lista.'''
def instruction_R(func7,rs2,rs1,func3,rd,opcode):
    instruction=[]
    cont=0
    # Agrega los bits del opcode al arreglo de instrucciones
    # El método append() solo agrega un elemento por vez.
    while cont < 7:
        instruction.append(opcode[-1])
        opcode=opcode[:-1]
        cont+=1
        # Agrega los bits correspondientes al registro de destino (rd)
    while cont < 12:
        if (not rd):
            instruction.append('0')
        elif(rd[-1]=='b'):
            instruction.append('0')
        else:
            instruction.append(rd[-1])
        rd=rd[:-1]
        cont+=1
        #func3
    while cont < 15:
        instruction.append(func3[-1])
        func3=func3[:-1]
        cont+=1
        #rs1
    while cont < 20:
        if (not rs1):
            instruction.append('0')
        elif(rs1[-1]=='b'):
            instruction.append('0')
        else:
            instruction.append(rs1[-1])
        rs1=rs1[:-1]
        cont+=1
        #rs2
    while cont < 25:
        if (not rs2):
            instruction.append('0')
        elif(rs2[-1]=='b'):
            instruction.append('0')
        else:
            instruction.append(rs2[-1])
        rs2=rs2[:-1]
        cont+=1
        #func7
    while cont < 32:
        instruction.append(func7[-1])
        func7=func7[:-1]
        cont+=1
    return instruction

'''Genera una instrucción de tipo I en formato binario.'''
def instruction_I(isNeg,imm,rs1,func3,rd,opcode):
    instruction=[]
    cont=0
    while cont < 7:
        instruction.append(opcode[-1])
        opcode=opcode[:-1]
        cont+=1
    while cont < 12:
        if(not rd): #si esta vacio
            instruction.append('0')
        elif(rd[-1]=='b'):
            instruction.append('0')
        else:
            instruction.append(rd[-1])
        rd=rd[:-1]
        cont+=1
    while cont < 15:
        instruction.append(func3[-1])
        func3=func3[:-1]
        cont+=1
    while cont < 20:
        if (not rs1):
            instruction.append('0')
        elif(rs1[-1]=='b'):
            instruction.append('0')
        else:
            instruction.append(rs1[-1])
        rs1=rs1[:-1]
        cont+=1
    while cont < 32:
        if (not imm):
            if isNeg:
                instruction.append('1')
            else:
                instruction.append('0')
        elif(imm[-1]=='b'):
            if isNeg:
                instruction.append('1')
            else:
                instruction.append('0')
        else:
            instruction.append(imm[-1])
        imm=imm[:-1]
        cont+=1
    return instruction

'''Genera una instrucción de tipo S en formato binario.'''
def instruction_S(rs2,rs1,func3,imm,opcode):
    instruction=[]
    cont=0
    while cont < 7:
        instruction.append(opcode[-1])
        opcode=opcode[:-1]
        cont+=1
    while cont < 12:
        if(not imm): #si esta vacio
            instruction.append('0')
        elif(imm[-1]=='b'):
            instruction.append('0')
        else:
            instruction.append(imm[-1])
        imm=imm[:-1]
        cont+=1
    while cont < 15:
        instruction.append(func3[-1])
        func3=func3[:-1]
        cont+=1
    while cont < 20:
        if (not rs1):
            instruction.append('0')
        elif(rs1[-1]=='b'):
            instruction.append('0')
        else:
            instruction.append(rs1[-1])
        rs1=rs1[:-1]
        cont+=1
    while cont < 25:
        if (not rs2):
            instruction.append('0')
        elif(rs2[-1]=='b'):
            instruction.append('0')
        else:
            instruction.append(rs2[-1])
        rs2=rs2[:-1]
        cont+=1
    while cont < 32:
        if(not imm): #si esta vacio
            instruction.append('0')
        elif(imm[-1]=='b'):
            instruction.append('0')
        else:
            instruction.append(imm[-1])
        imm=imm[:-1]
        cont+=1
    return instruction

'''Genera una instrucción de tipo B en formato binario.'''
def instruction_B(isNeg,rs2,rs1,func3,label,opcode):
    instruction=[]
    cont=0
    'Opcode (7 bits):'
    while cont < 7:
        instruction.append(opcode[-1])
        opcode=opcode[:-1]
        cont+=1
        'Bit 11 del inmediato (imm[11])'
    if len(label)>=11 and label[-10]!='b':
        instruction.append(label[-10])
    else:
        if isNeg:
            instruction.append('1')
        else:
            instruction.append('0')
    cont+=1
    label=label[:-1]
    'Bits 4:1 del inmediato (imm[4:1]):'
    while cont < 12:
        if(not label): #si esta vacio
            instruction.append('0')
        elif(label[-1]=='b'):
            instruction.append('0')
        else:
            instruction.append(label[-1])
        label=label[:-1]
        cont+=1
        ''
    'funct3 (3 bits)'
    while cont < 15:
        instruction.append(func3[-1])
        func3=func3[:-1]
        cont+=1
    'Registro rs1 (5 bits)'
    while cont < 20:
        if (not rs1):
            instruction.append('0')
        elif(rs1[-1]=='b'):
            instruction.append('0')
        else:
            instruction.append(rs1[-1])
        rs1=rs1[:-1]
        cont+=1
    'Registro rs2 (5 bits)'
    while cont < 25:
        if (not rs2):
            instruction.append('0')
        elif(rs2[-1]=='b'):
            instruction.append('0')
        else:
            instruction.append(rs2[-1])
        rs2=rs2[:-1]
        cont+=1
    'Bits 10:5 del inmediato (imm[10:5])'
    while cont < 31:
        if (not label):
            if isNeg:
                instruction.append('1')
            else:
                instruction.append('0')
        elif(label[-1]=='b'):
            if isNeg:
                instruction.append('1')
            else:
                instruction.append('0')
        else:
            instruction.append(label[-1])
        label=label[:-1]
        cont+=1
    'Bit 12 del inmediato (imm[12] byte mas significativo)'
    label=label[:-1]
    if (not label):
        if isNeg:
            instruction.append('1')
        else:
            instruction.append('0')
    else:
        instruction.append(label[-1])
    return instruction

def instruction_U(isNeg,label,rd,opcode):
    instruction=[]
    cont=0
    while cont < 7:
        instruction.append(opcode[-1])
        opcode=opcode[:-1]
        cont+=1
    while cont < 12:
        if(not rd): #si esta vacio
            instruction.append('0')
        elif(rd[-1]=='b'):
            instruction.append('0')
        else:
            instruction.append(rd[-1])
        rd=rd[:-1]
        cont+=1
        'Inmediato de 20 bits (imm[31:12]):'
    for i in range(12):
        label=label[:-1]

    while cont < 32:
        if (not label):
            if isNeg:
                instruction.append('1')
            else:
                instruction.append('0')
        elif(label[-1]=='b'):
            if isNeg:
                instruction.append('1')
            else:
                instruction.append('0')
        else:
            instruction.append(label[-1])
        label=label[:-1]
        cont+=1
    return instruction

def instruction_J(isNeg,label,rd,opcode):
    instruction=[]
    cont=0
    while cont < 7:
        instruction.append(opcode[-1])
        opcode=opcode[:-1]
        cont+=1
    while cont < 12:
        if(not rd): #si esta vacio
            instruction.append('0')
        elif(rd[-1]=='b'):
            instruction.append('0')
        else:
            instruction.append(rd[-1])
        rd=rd[:-1]
        cont+=1
    label=label[:-1]
    'Crea copias para manejar los bits dispersos del offset'
    label_copy1=label
    label_copy2=label
    label_copy3=label
    'Bits 10:1 del offset:'
    for i in range(11):
        label=label[:-1]
    
    while cont < 20:
        if (not label):
            if isNeg:
                instruction.append('1')
            else:
                instruction.append('0')
        elif(label[-1]=='b'):
            if isNeg:
                instruction.append('1')
            else:
                instruction.append('0')
        else:
            instruction.append(label[-1])
        label=label[:-1]
        cont+=1
    'Bit 11 del offset:'
    for i in range(10):
        label_copy1=label_copy1[:-1]
    if (not label_copy1):
        if isNeg:
            instruction.append('1')
        else:
            instruction.append('0')
    elif(label_copy1[-1]=='b'):
        if isNeg:
            instruction.append('1')
        else:
            instruction.append('0')
    else:
        instruction.append(label_copy1[-1])
    cont+=1
    'Bits 19:12 del offset:'
    while cont < 31:
        if (not label_copy2):
            if isNeg:
                instruction.append('1')
            else:
                instruction.append('0')
        elif(label_copy2[-1]=='b'):
            if isNeg:
                instruction.append('1')
            else:
                instruction.append('0')
        else:
            instruction.append(label_copy2[-1])
        label_copy2=label_copy2[:-1]
        cont+=1

    for i in range(19):
        label_copy3=label_copy3[:-1]

    if (not label_copy3):
        if isNeg:
            instruction.append('1')
        else:
            instruction.append('0')
    elif(label_copy3[-1]=='b'):
        if isNeg:
            instruction.append('1')
        else:
            instruction.append('0')
    else:
        instruction.append(label_copy3[-1])
    return instruction
# Funciones instruction_U y instruction_J son similares con sus respectivos formatos.

'''Convierte un valor inmediato negativo a su complemento a 2.'''
'''Convertidor de los negativos en los inmediatos'''
def converter_A2Complement(imm):
    new_imm=""
    firstOneBurned=False
     # Proceso de complemento a 2
    if(imm[-1]=='1'):
        new_imm=imm[-1]+new_imm
        imm=imm[:-1]
        firstOneBurned=True

    while imm[-1]!='b':
        if (firstOneBurned):
            if(imm[-1]=='1'):
                new_imm='0'+new_imm
            else:
                new_imm='1'+new_imm
        else:
            new_imm=imm[-1]+new_imm
        if(imm[-1]=='1'):
            firstOneBurned=True
        imm=imm[:-1]
    return new_imm

'''Invierte los elementos de una lista.'''
'''lo que esta de ultimo queda de primero y viceversa vector'''
def flip_array(array):
    l1=[]
    count=1
    for e in array:
        l1.append(array[-count])
        count+=1
    return l1


"""
    Este bloque principal se encarga de realizar las siguientes tareas:
    
    1. Definir los diccionarios necesarios para traducir las instrucciones de RISC-V a su representación en bits:
        - TypeList: Lista que asocia cada tipo de instrucción con sus respectivas operaciones (mnemonics).
        - Dictionary_OpCode: Diccionario que asocia cada tipo de instrucción con su código de operación (opcode).
        - Dictionary_Func3: Diccionario que asocia las instrucciones con sus correspondientes códigos 'func3'.
        - Dictionary_Func7: Diccionario que asocia las instrucciones de tipo R con su código 'func7'.
        - Dictionary_Hexadecimal: Diccionario que mapea combinaciones de 4 bits a su representación hexadecimal.

    2. Leer un archivo de entrada "EntradaRiscV.txt" que contiene las instrucciones RISC-V.

    3. Para cada línea del archivo de entrada:
        - Se divide la línea en sus componentes (mnemonic, registros, inmediatros, etc.).
        - Se identifica el tipo de instrucción (R, I, S, B, J, U) y se obtienen sus correspondientes opcodes y campos de función.
        - Se convierte la instrucción en una secuencia de bits de 32 bits, dependiendo del tipo de instrucción.
        - Se transforma la secuencia de bits en su representación hexadecimal.
        - Se escribe el resultado hexadecimal en un archivo de salida "SalidaHexa.txt".
    
    Validaciones específicas:
    - Se consideran instrucciones de tipo R, I, S, B, J y U, así como variantes específicas como 'L', 'IJ', 'Ului' y 'Uauipc'.
    - En caso de que los valores inmediatos sean negativos, se convierte el valor al complemento a dos.
    - Se realiza un volteo de bits (flip_array) antes de generar el valor hexadecimal.

    El resultado final es un archivo "SalidaHexa.txt" que contiene las instrucciones en formato hexadecimal.

    """




if __name__ =="__main__":
    # Definiciones de los diccionarios con los tipos de instrucciones, opcodes, func3, func7, y la conversión a hexadecimal

    TypeList = {
    'R':["add","sub","sll","slt","sltu","xor","srl","sra","or","and"],

    'I':["addi","slli","slti","sltiu","xori","srli","srai","ori","andi"],

    "IJ":["jalr"],

    'L':["lb","lh","lw","lbu","lhu"],

    'J':["jal"],

    'Ului':["lui"],

    'Uauipc':["auipc"],

    'S':["sb","sh","sw"],

    'B':["beq","bne","blt","bge","bltu","bgeu"]
    }

    Dictionary_OpCode = {
    'R':"0110011",
    'I':"0010011",
    'L':"0000011",
    'IJ':"1100111",
    'S':"0100011",
    'B':"1100011",
    'J':"1101111",
    'Ului':"0110111",
    'Uauipc':"0010111"
    }

    Dictionary_Func3 = {
    "add":"000",
    "sub":"000",
    "sll":"001",
    "slt":"010",
    "sltu":"011",
    "xor":"100",
    "srl":"101",
    "sra":"101",
    "or":"110",
    "and":"111",

    "addi":"000",
    "slli":"001",
    "slti":"010",
    "sltiu":"011",
    "xori":"100",
    "srli":"101",
    "srai":"101",
    "ori":"110",
    "andi":"111",

    "lb":"000",
    "lh":"001",
    "lw":"010",
    "lbu":"100",
    "lhu":"101",

    "jalr":"000",

    "beq":"000",
    "bne":"001",
    "blt":"100",
    "bge":"101",
    "bltu":"110",
    "bgeu":"111",

    "sb":"000",
    "sh":"001",
    "sw":"010",

    "jal":"000",
    "lui":"000",
    "auipc":"000"
    }

    Dictionary_Func7 = {
    "add":"0000000",
    "sub":"0100000",
    "sll":"0000000",
    "slt":"0000000",
    "sltu":"0000000",
    "xor":"0000000",
    "srl":"0000000",
    "sra":"0100000",
    "or":"0000000",
    "and":"0000000",

    "addi":"0000000",
    "slli":"0000000",
    "slti":"0000000",
    "sltiu":"0000000",
    "xori":"0000000",
    "srli":"0000000",
    "srai":"0000000",
    "ori":"0000000",
    "andi":"0000000",

    "lb":"0000000",
    "lh":"0000000",
    "lw":"0000000",
    "lbu":"0000000",
    "lhu":"0000000",

    "jalr":"0000000",

    "beq":"0000000",
    "bne":"0000000",
    "blt":"0000000",
    "bge":"0000000",
    "bltu":"0000000",
    "bgeu":"0000000",

    "sb":"0000000",
    "sh":"0000000",
    "sw":"0000000",

    "jal":"0000000",
    "lui":"0000000",
    "auipc":"0000000"
    }

    Dictionary_Hexadecimal = {
    "0000":"0",
    "0001":"1",
    "0010":"2",
    "0011":"3",
    "0100":"4",
    "0101":"5",
    "0110":"6",
    "0111":"7",
    "1000":"8",
    "1001":"9",
    "1010":"A",
    "1011":"B",
    "1100":"C",
    "1101":"D",
    "1110":"E",
    "1111":"F",
    }
    '''Hacemos las validaciones de las intrucciones de riscV'''
    instruction_32bits=[] # Lista que contendrá la instrucción en formato de 32 bits.
    linesList=[] # Lista para almacenar las líneas del archivo de entrada.
    # Abrimos el archivo de entrada que contiene las instrucciones RISC-V.
    with open("EntradaRiscV.txt",'r') as Input:
        linesList=Input.readlines() # Leemos todas las líneas del archivo.
        # Procesamos cada línea del archivo.
        for line in linesList:
            elements=line.split(",") # Dividimos cada línea por comas para extraer los componentes.
            elements=takeJumpAwayArray(elements) # Eliminamos elementos innecesarios de la línea.
              # Identificamos el tipo de instrucción (R, I, S, etc.) y obtenemos sus campos correspondientes.
            type=find_the_type(TypeList,elements[0])# elements[0] contiene el mnemonico de la instrucción.
            opcode=(Dictionary_OpCode[type])# Obtenemos el código de operación (opcode).
            func3=(Dictionary_Func3[elements[0]]) #func3
            func7=(Dictionary_Func7[elements[0]]) #func7 
            # Inicializamos los registros y valores inmediatos necesarios.
            rd=""
            rs1=""
            rs2=""
            imm=""
            isNeg=False  #Variable para manejar si el valor inmediato es negativo.

             # Procesamos las instrucciones de tipo 'R'.
            if(type=='R'):
                rd=bin(decode_identifier(elements[1]))  #Decodificamos el registro destino (rd) a binario.
                rs1=bin(decode_identifier(elements[2])) # Decodificamos el registro fuente 1 (rs1).
                rs2=bin(decode_identifier(elements[3])) # Decodificamos el registro fuente 2 (rs2).
                instruction_32bits=instruction_R(func7,rs2,rs1,func3,rd,opcode) # Construimos la instrucción de tipo R.
                #ahora lo voltea  ,Invertimos el array de bits para generar el formato correcto.
                inst32bf = flip_array(instruction_32bits) #instruccion de 32bits volteada

                # Convertimos la instrucción de 32 bits a hexadecimal.
                cont=0
                Hexa=""
                for i in range(8): # Procesamos cada 4 bits para obtener su equivalente hexadecimal.
                    temp=inst32bf[cont]+inst32bf[cont+1]+inst32bf[cont+2]+inst32bf[cont+3]
                    Hplus=Dictionary_Hexadecimal[temp]
                    Hexa = Hexa + Hplus
                    cont+=4
                 # Escribimos el valor hexadecimal de la instrucción en el archivo de salida.    
                with open("SalidaHexa.txt",'a') as Output:
                    Output.write(Hexa)
                    Output.write("\n")
                #Procesamos las instrucciones de tipo 'I', 'L', o 'IJ'.    
            if (type=='I' or type=='L' or type=='IJ'):
                rd=bin(decode_identifier(elements[1])) # Decodificamos el registro destino (rd).
                if (type=='I'):
                    rs1=bin(decode_identifier(elements[2])) # Decodificamos el registro fuente (rs1).
                    imm=bin(decode_identifier(elements[3])) # Decodificamos el valor inmediato.
                else:
                    imm=bin(decode_identifier(elements[2])) # En caso de ser 'L' o 'IJ', se invierten los parámetros.
                    rs1=bin(decode_identifier(elements[3]))

                 # Si el inmediato es negativo, convertimos a complemento a 2.
                if(imm[0]=='-'):
                    isNeg=True
                    imm=converter_A2Complement(imm)

                # Construimos la instrucción de tipo I.
                instruction_32bits=instruction_I(isNeg,imm,rs1,func3,rd,opcode)
                inst32bf = flip_array(instruction_32bits)

                # Convertimos a hexadecimal y escribimos en el archivo de salida.
                cont=0
                Hexa=""
                for i in range(8):
                    temp=inst32bf[cont]+inst32bf[cont+1]+inst32bf[cont+2]+inst32bf[cont+3]
                    Hplus=Dictionary_Hexadecimal[temp]
                    Hexa = Hexa + Hplus
                    cont+=4
                with open("SalidaHexa.txt",'a') as Output:
                    Output.write(Hexa)
                    Output.write("\n")
                # Procesamos las instrucciones de tipo 'S'.    
            if (type=='S'):
                rs2=bin(decode_identifier(elements[1])) # Decodificamos el registro fuente 2 (rs2).
                imm=bin(decode_identifier(elements[2])) # Decodificamos el valor inmediato.
                rs1=bin(decode_identifier(elements[3])) # Decodificamos el registro fuente 1 (rs1).

                # Construimos la instrucción de tipo S.
                #tipo 'S' el inm nunca es negativo
                instruction_32bits=instruction_S(rs2,rs1,func3,imm,opcode)
                inst32bf = flip_array(instruction_32bits)

                 # Convertimos a hexadecimal y escribimos en el archivo de salida.
                cont=0
                Hexa=""

                # Procesamos las instrucciones de tipo 'B'.
                for i in range(8):
                    temp=inst32bf[cont]+inst32bf[cont+1]+inst32bf[cont+2]+inst32bf[cont+3]
                    Hplus=Dictionary_Hexadecimal[temp]
                    Hexa = Hexa + Hplus
                    cont+=4
                with open("SalidaHexa.txt",'a') as Output:
                    Output.write(Hexa)
                    Output.write("\n")
                    'saltos'
            if(type=='B'):
                rs1=bin(decode_identifier(elements[1]))
                rs2=bin(decode_identifier(elements[2]))
                label=bin(decode_identifier(elements[3])*4) 

                # Si el inmediato es negativo, convertimos a complemento a 2.
                if(label[0]=='-'):
                    isNeg=True
                    label=converter_A2Complement(label)

                instruction_32bits=instruction_B(isNeg,rs2,rs1,func3,label,opcode)
                inst32bf = flip_array(instruction_32bits)
                cont=0
                Hexa=""
                for i in range(8):
                    temp=inst32bf[cont]+inst32bf[cont+1]+inst32bf[cont+2]+inst32bf[cont+3]
                    Hplus=Dictionary_Hexadecimal[temp]
                    Hexa = Hexa + Hplus
                    cont+=4
                with open("SalidaHexa.txt",'a') as Output:
                    Output.write(Hexa)
                    Output.write("\n")

                 # Procesamos las instrucciones de tipo 'U' (lui o auipc).
            if (type=='Ului' or type=='Uauipc'):
                rd=bin(decode_identifier(elements[1]))
                label=bin(decode_identifier(elements[2])*4)
                if(label[0]=='-'):
                    isNeg=True
                    label=converter_A2Complement(label)

                instruction_32bits=instruction_U(isNeg,label,rd,opcode)
                inst32bf = flip_array(instruction_32bits)
                cont=0
                Hexa=""
                for i in range(8):
                    temp=inst32bf[cont]+inst32bf[cont+1]+inst32bf[cont+2]+inst32bf[cont+3]
                    Hplus=Dictionary_Hexadecimal[temp]
                    Hexa = Hexa + Hplus
                    cont+=4
                with open("SalidaHexa.txt",'a') as Output:
                    Output.write(Hexa)
                    Output.write("\n")
                    
                # Procesamos las instrucciones de tipo 'J' (jal).    
            if(type=='J'):
                rd=bin(decode_identifier(elements[1]))
                label=bin(decode_identifier(elements[2])*4)
                if(label[0]=='-'):
                    isNeg=True
                    label=converter_A2Complement(label)

                instruction_32bits=instruction_J(isNeg,label,rd,opcode)
                inst32bf = flip_array(instruction_32bits)
                cont=0
                Hexa=""
                for i in range(8):
                    temp=inst32bf[cont]+inst32bf[cont+1]+inst32bf[cont+2]+inst32bf[cont+3]
                    Hplus=Dictionary_Hexadecimal[temp]
                    Hexa = Hexa + Hplus
                    cont+=4
                with open("SalidaHexa.txt",'a') as Output:
                    Output.write(Hexa)
                    Output.write("\n")

    # Inicia la lectura del archivo de entrada y proceso de instrucciones
    print("\n\n Se ha generado las instrucciones. \n")


