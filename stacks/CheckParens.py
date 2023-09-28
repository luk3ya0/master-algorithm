from LinkedStack import LinkedStack


class CheckParens(object):
    @staticmethod
    def check(text) -> bool:
        parens = "()[]{}"
        openParens = "([{"
        opposites = {
            ")": "(",
            "]": "[",
            "}": "{",
        }

        def parentheses():
            step, stop = 0, len(text)
            while True:
                while step < stop and text[step] not in parens:
                    step += 1
                if step >= stop:
                    return

                yield text[step], step
                step += 1

        linkedStack = LinkedStack()
        for pr, idx in parentheses():
            if pr in openParens:
                linkedStack.push(pr)
            elif linkedStack.pop() != opposites[pr]:
                return False
            else:
                pass

        return True
