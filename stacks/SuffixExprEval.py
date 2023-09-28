from LinkedStack import LinkedStack


class SuffixExprEval(object):
    @staticmethod
    def eval(expr: str):
        operators = "+-*/"
        linkedStack = LinkedStack()

        for obj in expr.split():
            if obj not in operators:
                linkedStack.push(float(obj))
                continue

            if linkedStack.depth < 2:
                raise SyntaxError("Short of operands(s).")

            car = linkedStack.pop()
            cdr = linkedStack.pop()

            if obj == "+":
                res = car + cdr
            elif obj == "-":
                res = car - cdr
            elif obj == "*":
                res = car * cdr
            elif obj == "/":  # divided by zero
                res = car / cdr
            else:
                break

            linkedStack.push(res)

        if linkedStack.depth == 1:
            return linkedStack.pop()

        raise SyntaxError("Extra operand(s).")
