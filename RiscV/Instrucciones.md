ML_Traductor
Bien, este es un traductor que convierte de LENGUAJE DE BAJO NIVEL INSTRUCCIONES DE RISC-V a LENGUAJE DE MÁQUINA HEXADECIMAL

la rama «fully_functional_translator» es la más actualizada

¿CÓMO FUNCIONA?

en el fichero «Entrada.txt» escribes las instrucciones RISC-V línea a línea, luego ejecutas el código principal y volià, las instrucciones hexadecimales aparecerán en el fichero «OutputSampleHex»

CÓMO DEBES ESCRIBIR LAS INSTRUCCIONES EN LENGUAJE DE BAJO NIVEL

sigues el estándar RISC-V pero cada elemento de la sentencia debe ir separado por una coma (,)

EJEMPLO, si quieres escribir: addi sp, sp, -20

se escribe: addi,sp,sp,-20

OTROS EJEMPLOS: sw x8, 0(sp) -> sw,x8,0,sp

jalr x0, 0(ra) -> jalr,x0,0,ra

jal -7 -> jal,x1,-7 //Sé que 'x1' en este caso está implícito pero debe ser explícito para que este código funcione correctamente

LOS SALTOS

en las instrucciones de rama simplemente se introduce la cantidad de saltos necesarios para pasar de la línea A a la línea B

es decir, si tienes

0x...4024 for0: bge, x18, x9, endfor0 . . .

0x...4068 endfor0: ...

si restas los números hexadecimales 4068 - 4024 = obtienes 44, lo conviertes a base decimal y es 68, lo divides por 4 y es 17

entonces, 17 es el número que debes escribir en la instrucción: bge, x18, x9, 17

¿Por qué?

Bueno, para un procesador direccionado por Byte, una instrucción se guarda en realidad en 4 líneas de memoria, pero en la vida real sólo tienes que contar las líneas entre instrucciones.

lo mismo ocurre con los saltos negativos (saltos hacia atrás) si tienes -68 en base decimal, escribes -17 en la instrucción de tipo B

TE GARANTIZO QUE ESTE PROGRAMA FUNCIONA 100% PERFECTAMENTE PARA CUALQUIER INSTRUCCIÓN DE TIPO R,T,S,B,J SEGÚN LA ARQUITECTURA RISC-V DE 32-bits.

las unicas 2 insturcciones para las cuales no garantizo calidad son 'lui' y 'auipc' nunca las he usado y no las conozco profundamente, asumi que las Imm para tipo U hacen saltos de la misma manera que 'jal', asi que la logica es la misma especificada arriba.

Espero que esto te sea útil.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

A continuación se presenta la descripción de cada línea de las instrucciones RISC-V mencionadas, así como su clasificación según el tipo de instrucción:

1. addi sp, sp, -20
Descripción: Resta 20 al valor actual del registro sp (stack pointer) y guarda el resultado en sp.
Tipo: Instrucción de tipo I (inmediata), aritmética.
2. sw x8, 0(sp)
Descripción: Almacena el valor del registro x8 en la dirección de memoria a la que apunta sp con un offset de 0.
Tipo: Instrucción de tipo S (almacenamiento).
3. sw x9, 4(sp)
Descripción: Almacena el valor del registro x9 en la dirección de memoria sp + 4.
Tipo: Instrucción de tipo S (almacenamiento).
4. sw x18, 8(sp)
Descripción: Almacena el valor del registro x18 en la dirección de memoria sp + 8.
Tipo: Instrucción de tipo S (almacenamiento).
5. sw x19, 12(sp)
Descripción: Almacena el valor del registro x19 en la dirección de memoria sp + 12.
Tipo: Instrucción de tipo S (almacenamiento).
6. sw x20, 16(sp)
Descripción: Almacena el valor del registro x20 en la dirección de memoria sp + 16.
Tipo: Instrucción de tipo S (almacenamiento).
7. addi x8, x10, 0
Descripción: Copia el valor del registro x10 en el registro x8 (suma x10 con 0).
Tipo: Instrucción de tipo I (inmediata), aritmética.
8. addi x9, x11, 0
Descripción: Copia el valor del registro x11 en el registro x9.
Tipo: Instrucción de tipo I (inmediata), aritmética.
9. addi x18, x0, 0
Descripción: Copia el valor del registro x0 (siempre 0) en x18.
Tipo: Instrucción de tipo I (inmediata), aritmética.
10. bge x18, x9, 17
Descripción: Salta a la instrucción ubicada 17 líneas más abajo si x18 es mayor o igual que x9.
Tipo: Instrucción de tipo B (condicional de rama).
11. addi x19, x0, 0
Descripción: Copia el valor del registro x0 en x19.
Tipo: Instrucción de tipo I (inmediata), aritmética.
12. sub x21, x9, x18
Descripción: Resta el valor de x18 de x9 y almacena el resultado en x21.
Tipo: Instrucción de tipo R (aritmética).
13. addi x21, x21, -1
Descripción: Resta 1 al valor de x21.
Tipo: Instrucción de tipo I (inmediata), aritmética.
14. bge x19, x21, 11
Descripción: Salta a la instrucción ubicada 11 líneas más abajo si x19 es mayor o igual que x21.
Tipo: Instrucción de tipo B (condicional de rama).
15. slli x5, x19, 2
Descripción: Realiza un desplazamiento lógico a la izquierda (shift left) de x19 por 2 posiciones, y guarda el resultado en x5.
Tipo: Instrucción de tipo I (inmediata), desplazamiento.
16. add x22, x8, x5
Descripción: Suma el valor de x8 con x5 y almacena el resultado en x22.
Tipo: Instrucción de tipo R (aritmética).
17. lw x23, 0(x22)
Descripción: Carga el valor de la dirección de memoria x22 + 0 en el registro x23.
Tipo: Instrucción de tipo I (carga).
18. lw x24, 4(x22)
Descripción: Carga el valor de la dirección de memoria x22 + 4 en el registro x24.
Tipo: Instrucción de tipo I (carga).
19. blt x23, x24, 4
Descripción: Salta a la instrucción ubicada 4 líneas más abajo si x23 es menor que x24.
Tipo: Instrucción de tipo B (condicional de rama).
20. addi x20, x23, 0
Descripción: Copia el valor de x23 en x20.
Tipo: Instrucción de tipo I (inmediata), aritmética.
21. addi x23, x24, 0
Descripción: Copia el valor de x24 en x23.
Tipo: Instrucción de tipo I (inmediata), aritmética.
22. addi x24, x20, 0
Descripción: Copia el valor de x20 en x24.
Tipo: Instrucción de tipo I (inmediata), aritmética.
23. addi x19, x19, 1
Descripción: Suma 1 al valor de x19.
Tipo: Instrucción de tipo I (inmediata), aritmética.
24. beq x0, x0, -10
Descripción: Salta a la instrucción ubicada 10 líneas atrás si x0 es igual a x0 (instrucción incondicional).
Tipo: Instrucción de tipo B (condicional de rama, en este caso siempre verdadera).
25. addi x18, x18, 1
Descripción: Suma 1 al valor de x18.
Tipo: Instrucción de tipo I (inmediata), aritmética.
26. beq x0, x0, -16
Descripción: Salta a la instrucción ubicada 16 líneas atrás si x0 es igual a x0 (instrucción incondicional).
Tipo: Instrucción de tipo B (condicional de rama).
27. lw x8, 0(sp)
Descripción: Carga el valor de la dirección de memoria sp + 0 en el registro x8.
Tipo: Instrucción de tipo I (carga).
28. lw x9, 4(sp)
Descripción: Carga el valor de la dirección de memoria sp + 4 en el registro x9.
Tipo: Instrucción de tipo I (carga).
29. lw x18, 8(sp)
Descripción: Carga el valor de la dirección de memoria sp + 8 en el registro x18.
Tipo: Instrucción de tipo I (carga).
30. lw x19, 12(sp)
Descripción: Carga el valor de la dirección de memoria sp + 12 en el registro x19.
Tipo: Instrucción de tipo I (carga).
31. lw x20, 16(sp)
Descripción: Carga el valor de la dirección de memoria sp + 16 en el registro x20.
Tipo: Instrucción de tipo I (carga).
32. addi sp, sp, 20
Descripción: Suma 20 al valor actual del registro sp y guarda el resultado en sp.
Tipo: Instrucción de tipo I (inmediata), aritmética.
33. jalr x0, 0(ra)
Descripción: Salta a la dirección almacenada en ra (registro de retorno) y almacena la dirección de la instrucción siguiente en x0.
Tipo: Instrucción de tipo I (salto).
34. jal x1, -7
Descripción: Salta a la instrucción ubicada 7 líneas atrás y guarda la dirección de la siguiente instrucción en x1.
Tipo: Instrucción de tipo J (salto).
Esto cubre toda la lista de instrucciones RISC-V proporcionada, indicando su tipo y función.


------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Estos diccionarios son estructuras que mapean diferentes componentes de las instrucciones de ensamblado RISC-V a sus equivalentes binarios o hexadecimales. A continuación te explico cada uno de ellos:

Dictionary_OpCode:

Este diccionario asocia el tipo de instrucción RISC-V (como R, I, L, etc.) con su código de operación binario (opcode). El opcode es un conjunto de bits que indica el tipo de operación que la instrucción realiza.
Ejemplo:
'R': "0110011" indica que las instrucciones de tipo R tienen el opcode binario 0110011.
Dictionary_Func3:

Este diccionario mapea el mnemonico de una instrucción (como add, sub, lw, jalr, etc.) a su campo func3 correspondiente en binario. El campo func3 es parte de las instrucciones que especifican cómo se deben comportar ciertas operaciones.
Ejemplo:
"add": "000" significa que la instrucción add tiene el valor de func3 igual a 000.
"beq": "000" significa que la instrucción beq también tiene el valor de func3 igual a 000.
Dictionary_Func7:

Este diccionario asocia las instrucciones con su campo func7. El campo func7 es utilizado en algunas instrucciones (principalmente de tipo R) para definir detalles adicionales de la operación, como diferencias entre instrucciones similares (por ejemplo, add y sub).
Ejemplo:
"add": "0000000" indica que la instrucción add tiene func7 igual a 0000000.
"sub": "0100000" indica que la instrucción sub tiene func7 igual a 0100000, lo que la diferencia de add.
Dictionary_Hexadecimal:

Este diccionario mapea grupos de 4 bits (nibbles) a su correspondiente representación hexadecimal. Se utiliza cuando se necesitan convertir secuencias de bits a su formato hexadecimal para simplificar la representación de las instrucciones.
Ejemplo:
"0000": "0" significa que el valor binario 0000 corresponde al dígito hexadecimal 0.
"1010": "A" significa que el valor binario 1010 corresponde al dígito hexadecimal A.
Estos diccionarios facilitan la conversión de instrucciones RISC-V en formato ensamblador a su correspondiente representación binaria y hexadecimal para su posterior uso en procesadores.


---------------------------------------------------------------------------------------------------

decode_identifier: Conversión de Nombres de Registros
¿Qué hace?
Convierte los nombres simbólicos de registros RISC-V (como 'ra', 'sp', 'x1') a sus valores numéricos equivalentes.

Cómo funciona:

Maneja casos especiales primero ('ra' y 'sp')

Para otros registros, elimina la 'x' y convierte el número a entero

-------------------------------------------------------------------------------------------------------
El código:

Asume que mi_label ya fue definida (tu ensamblador no verifica esto actualmente).

Convierte la label a un offset numérico usando decode_identifier(elements[3])*4 (para saltos)