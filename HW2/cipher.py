def encrypt(inputText, N, D):
    # Validate inputs
    if not isinstance(inputText, str) or not isinstance(N, int):
        return ""
    if N < 1 or D not in [1, -1]:
        return ""
    if any(ord(c) < 34 or ord(c) > 126 for c in inputText):
        return ""

    # Reverse text and shift each character within ASCII 34-126
    result = ""
    for char in inputText[::-1]:
        shifted = ((ord(char) - 34 + D * N) % 93) + 34
        result += chr(shifted)

    return result


def decrypt(encryptedText, N, D):
    # Validate inputs
    if not isinstance(encryptedText, str) or not isinstance(N, int):
        return ""
    if N < 1 or D not in [1, -1]:
        return ""
    if any(ord(c) < 34 or ord(c) > 126 for c in encryptedText):
        return ""

    # Shift back in opposite direction and reverse
    result = ""
    for char in encryptedText:
        shifted = ((ord(char) - 34 - D * N) % 93) + 34
        result += chr(shifted)

    return result[::-1]
