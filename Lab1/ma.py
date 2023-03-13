import numexpr as np
def calculate(expression):
    if expression not in '+-$*' and '.' in expression:
        return float(expression)
    elif any(i.isalpha() for i in expression):
        return "400: Bad request"
    else:
        expression = expression.replace('$', '/')
        res = np.evaluate(expression)
        return res
print(calculate('10+5'))