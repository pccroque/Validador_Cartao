# Valida um número de cartão de crédito usando o algoritmo de Luhn
# e identifica a bandeira do cartão com base no número inicial.

def get_card_brand(card_number):
    """Identifica a bandeira do cartão com base no número inicial."""
    card_prefixes = {
        "MasterCard": [(51, 55), (2221, 2720)],
        "Visa": [(4, 4)],
        "American Express": [(34, 34), (37, 37)],
        "Diners Club": [(300, 305), (36, 36), (38, 38)],
        "Discover": [(6011, 6011), (622126, 622925), (644, 649), (65, 65)],
        "JCB": [(3528, 3589)],
        "EnRoute": [(2014, 2014), (2149, 2149)],
        "Voyager": [(8699, 8699)],
        "HyperCard": [(6062, 6062)],
        "Aura": [(50, 50)]
    }

    for brand, ranges in card_prefixes.items():
        for start, end in ranges:
            if str(card_number).startswith(tuple(str(i) for i in range(start, end + 1))):
                return brand

    return "Desconhecido"

def luhn_check(card_number):
    """Valida o número do cartão usando o algoritmo de Luhn."""
    digits = [int(d) for d in str(card_number)]
    
    # Dobrar os dígitos alternados começando pelo penúltimo
    for i in range(len(digits) - 2, -1, -2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9
    
    # Somar todos os dígitos
    total = sum(digits)
    
    # Verificar se a soma é divisível por 10
    return total % 10 == 0

def validate_credit_card(card_number):
    """Verifica se um cartão de crédito é válido e identifica sua bandeira."""
    brand = get_card_brand(card_number)
    valid = luhn_check(card_number)

    if valid:
        print(f"O número do cartão é válido e pertence à bandeira {brand}.")
    else:
        print(f"O número do cartão é inválido.")

# Exemplo de uso
card_number = "345405939246653"  # Exemplo de número de cartão
validate_credit_card(card_number)