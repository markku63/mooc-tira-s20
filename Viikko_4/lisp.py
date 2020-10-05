import re

def eval(s):
    stack = []
    ev_stack = []
    term = re.compile(r"^[0-9]+\)+")

    expr = s.split()
    for tok in expr:
        if tok == "(+" or tok == "(*":
            stack.append(tok)
        elif tok.isdecimal():
            stack.append(int(tok))
        elif term.match(tok): # numero + n loppusulkua
            stack.append(int(tok.rstrip(")")))
            # jokaista loppusulkua kohti suoritetaan laskutoimitus ja
            # työnnetään tulos takaisin pinoon
            for i in range(tok.count(")")):
                ev_stack.clear()
                while isinstance(stack[-1], int):
                    ev_stack.append(stack.pop())
                op  = stack.pop()
                if op == "(+":
                    stack.append(sum(ev_stack))
                elif op == "(*":
                    prod = 1
                    for i in ev_stack:
                        prod *= i
                    stack.append(prod)
                else:
                    raise RuntimeError("This program is broken")
        else: # syntax error
            raise ValueError("Incorrect expression")

    # Jos kaikki toimi oikein, niin tulos on pinon päällä
    return stack[-1]
    
if __name__ == "__main__":
    print(eval("(+ 1 2 3 4 5)")) # 15
    print(eval("(+ 5 (* 3 2) 7)")) # 18
    print(eval("(* (+ (+ 1 2) 3) (+ (* 4 5) 6 2))")) # 168