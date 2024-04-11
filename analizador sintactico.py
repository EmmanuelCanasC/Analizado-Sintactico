import re

# Definición de tokens
tokens = [
    ('NUMBER', r'\d+'),
    ('PLUS', r'\+'),
    ('MINUS', r'-'),
    ('TIMES', r'\*'),
    ('DIVIDE', r'/'),
    ('LPAREN', r'\('),
    ('RPAREN', r'\)'),
]

# Función para tokenizar la entrada
def tokenize(input_string):
    tokenized = []
    while input_string:
        for token_type, pattern in tokens:
            regex = re.compile(pattern)
            match = regex.match(input_string)
            if match:
                value = match.group(0)
                tokenized.append((token_type, value))
                input_string = input_string[len(value):].strip()
                break
        else:
            raise ValueError('Tokenización fallida en: {}'.format(input_string))
    return tokenized

# Ejemplo de uso
if __name__ == "__main__":
    input_string = input("Ingrese una expresión matemática: ")
    tokens = tokenize(input_string)
    print("Tokens:", tokens)
