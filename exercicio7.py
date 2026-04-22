"""Exercício 7 — Calculadora Segura com Exceções: Crie uma 
calculadora que opere em loop ( while True) solicitando dois 
números e uma operação (+, -, *, /). O programa deve tratar com 
try/except: entrada não numérica ( ValueError), divisão por zero
 ( ZeroDivisionError) e operação inválida. Use else para exibir o
   resultado quando não houver erro e finallypara exibir  
   "Operação processada." sempre. O usuário pode digitar "sair" 
   para encerrar."""


def calcular(num1, num2, operacao):
    if operacao == "+":
        return num1 + num2
    elif operacao == "-":
        return num1 - num2
    elif operacao == "*":
        return num1 * num2
    elif operacao == "/":
        return num1 / num2
    else:

        raise ValueError("Operação inválida.")

def main():
    print("=== Calculadora Segura ===")
    print("Digite 'sair' no Número 1 para encerrar.\n")
    
    while True:
        try:
            entrada1 = input("Número 1: ")
            if entrada1.lower() == "sair":
                break
            
            num1 = float(entrada1)
            
            num2 = float(input("Número 2: "))
            operacao = input("Operação (+, -, *, /): ")
            
            resultado = calcular(num1, num2, operacao)
            
        except ValueError:

            print("Erro: Entrada inválida ou operação não suportada!")
        except ZeroDivisionError:
            print("Erro: Divisão por zero!")
        else:
            print(f"Resultado: {resultado}")
        finally:
            print("Operação processada.\n")

if __name__ == "__main__":
    main()