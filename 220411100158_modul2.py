# -*- coding: utf-8 -*-
"""220411100158_Modul2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-FZyY1R1H9btlTCy9GnJuQykOWW4H30e

# **Nomor 1**
"""

def stack():
    s=[]
    return (s)
def push(s,data):
    s.append(data)
def pop(s):
    data=s.pop()
    return(data)
def peek(s):
    return(s[len(s)-1])
def isEmpty(s):
    return (s==[])
def size(s):
    return(len(s))


def infix_to_postfix(expr):
    kurung_buka = '({['
    kurung_tutup = ')}]'
    output = []
    operator_stack = []

    precedence = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '^': 3
    }

    # (9-2)/(4+1)}*5
    # output = []
    # operator_stack = [{]
    for token in expr:
        if token.isdigit():
            output.append(token)
        elif token in '+-*/^':
            while operator_stack and operator_stack[-1] != '(' and precedence.get(token, 0) <= precedence.get(operator_stack[-1], 0):
                output.append(operator_stack.pop())
            operator_stack.append(token)
        elif token in kurung_buka:
            operator_stack.append(token)
        elif token in kurung_tutup:
            while operator_stack[-1] != kurung_buka[kurung_tutup.index(token)]:
                output.append(operator_stack.pop())
            operator_stack.pop()

    while operator_stack:
        output.append(operator_stack.pop())

    postfix = ''.join(output)
    return postfix

def evaluate_postfix(expr):
    operand_stack = []

    for token in expr:
        if token.isdigit():
            operand_stack.append(float(token))
        elif token in '+-*/^':
            b = operand_stack.pop()
            a = operand_stack.pop()
            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            elif token == '/':
                result = a / b
            elif token == '^':
                result = a ** b
            operand_stack.append(result)

    return operand_stack.pop()


def paranthesesCheck(strMath):
    operandStack=stack()
    lenMath=len(strMath)
    openOperand='({['
    closeOperand=')}]'
    i=0
    Matched=True;
    while i<(lenMath):
        if strMath[i] in openOperand:
            push(operandStack,strMath[i])
        elif strMath[i] in closeOperand:
            if not (isEmpty(operandStack)):
                top=pop(operandStack)
                if openOperand.index(top)==closeOperand.index(strMath[i]):
                    Matched=Matched and True
                else:
                    Matched=Matched and False
                    print ('Kurung Buka dan Kurang Tutup tidak Cocok')
            else:
                Matched=Matched and False
                print('Jumlah Kurung Tutup lebih banyak')
        i=i+1
    if not(isEmpty(operandStack)):
        Matched=False
        print('Jumlah Kurung Buka Lebih banyak')
    if Matched:
        _ = infix_to_postfix(strMath)
        total = evaluate_postfix(_)
        print(f"infix = {strMath}; postfix = {_} total = {total}")
    else:
        return

for i in range(6):
    paranthesesCheck(input("Masukkan string operasi aritmatika = "))
    print()


# {(2-5)/(4-1)
# 9*(7-4)]
# (4-2)*(3*(7-3)]
# {(9-2)/(4+1)}*5
# (4-2)*{3*(7-3)}
# {5*(4/[7-5])}

"""# **Nomor 2**"""

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, data):
        self.items.insert(0, data)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def __repr__(self):
          return str(self.items)


def CPU():
    q = Queue()
    n = int(input("Jumlah Proses yang akan dijadwal di CPU : "))
    for i in range(n):
        proses = []
        nama_proses = input(f"Nama Proses ke-{i} : ")
        waktu_proses = int(input("Waktu Proses : "))
        proses.append(nama_proses)
        proses.append(waktu_proses)
        q.enqueue(proses)
    print(f"\nAntrian Proses : {q}")
    cpu = int(input("waktu proses CPU :"))
    print()

    iterasi = 1
    while not q.is_empty():
        print(f"Iterasi ke-{iterasi}")
        iterasi += 1
        d = q.dequeue()
        b = []
        sisa = d[1] - cpu
        b.append(d[0])
        b.append(sisa)
        if b[1] > 0:
            q.enqueue(b)
            print(f"\tProses {d[0]} Sedang Diproses, dan Sisa Waktu Proses {d[0]} = {sisa} ")
        else:
            print(f"\tProses {d[0]} Selesai")

        print(f"\tData proses yang tersisa : {q}")
CPU()