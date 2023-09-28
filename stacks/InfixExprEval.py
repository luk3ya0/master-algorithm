from LinkedStack import LinkedStack
from SuffixExprEval import SuffixExprEval


class InfixExprEval(object):
    priority = {
        "(": 1,
        "+": 3,
        "-": 3,
        "*": 5,
        "/": 5,
    }
    operators = "+-*/()"

    @staticmethod
    def eval(expr: str):
        return SuffixExprEval.eval(InfixExprEval.toSuffix(expr))

    @staticmethod
    def toSuffix(expr: str):
        operStack = LinkedStack()
        tempExprs = []

        for obj in InfixExprEval.tokens(expr):
            if obj not in InfixExprEval.operators:
                tempExprs.append(obj)
            elif operStack.isEmpty or obj == '(':
                operStack.push(obj)
            elif obj == ')':
                while not operStack.isEmpty and operStack.top != '(':
                    tempExprs.append(operStack.pop())
                if operStack.isEmpty:
                    raise SyntaxError("Missing '('.")

                operStack.pop()
            else:
                while (not operStack.isEmpty and
                       InfixExprEval.priority[operStack.top] >= InfixExprEval.priority[obj]):
                    tempExprs.append(operStack.pop())

                operStack.push(obj)

        while not operStack.isEmpty:
            if operStack.top == '(':
                raise SyntaxError("Extra '('.")
            tempExprs.append(operStack.pop())

        return "".join(tempExprs)

    @staticmethod
    def tokens(expr: str):
        step, stop = 0, len(expr)
        while step < stop:
            while expr[step].isspace():
                step += 1
            if step >= stop:
                break
            if expr[step] in InfixExprEval.operators:
                yield expr[step]
                step += 1
                continue

            bigStep = step + 1

            while (bigStep < stop and not expr[bigStep].isspace() and
                   expr[bigStep] not in InfixExprEval.operators):
                if expr[bigStep].lower() == 'e' and bigStep+1 < stop and expr[bigStep+1] == '-':
                    bigStep += 1

                bigStep += 1

            yield expr[step:bigStep]

            step = bigStep
