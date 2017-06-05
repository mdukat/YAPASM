# YAPASM
Yet Another Pseudo ASM - translator for brainfuck

## Usage
python3 yapasm.py [file_with_yapasm_code]

## Syntax
```
ADD n - append n in current cell\n
DEC n - substract n in current cell
LOOP - open the loop
EOLOOP - close the loop
PRINT - print current cell
GET - get the input, store in current cell
MOVEL n - increment data pointer
MOVER n - decrement data pointer
```

## Example
This one prints out all chars
```
ADD 10;

LOOP;
MOVER 1;
ADD 12;
MOVEL 1;
DEC 1;
EOLOOP;

MOVER 1;
ADD 7;

LOOP;
MOVER 1;
ADD 1;
PRINT;
MOVEL 1;
DEC 1;
EOLOOP;
