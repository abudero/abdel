import re

def validar_email(email):
    criterios_email = [
        (re.search(r'[A-Z]', email), 'Debe contener al menos un letra en mayúscula.'),
        (re.search(r"[0-9]", email), "Debe contener al menos un número."),
        (re.search(r"[_$%&*.]", email), "Debe contener al menos un carácter especial (_$%&*)."),
        (re.search(r"[@]", email), "Debe contener el signo @.")

    ]
    errores = [mensaje for valido, mensaje in criterios_email if not valido]
    if errores:
        return "No apto:\n" + "\n".join(f"- {error}" for error in errores)
    return "Correo registrado. ¡Perfecto!"


def validar_contrasena(password):
    criterios = [
        (len(password) >= 8, "Debe tener al menos 8 caracteres."),
        (re.search(r"[a-z]", password), "Debe contener al menos una letra minúscula."),
        (re.search(r"[A-Z]", password), "Debe contener al menos una letra mayúscula."),
        (re.search(r"[0-9]", password), "Debe contener al menos un número."),
        (re.search(r"[_@$%&*]", password), "Debe contener al menos un carácter especial (_@$%&*)."),
    ]

    errores = [mensaje for valido, mensaje in criterios if not valido]
    if errores:
        return "Insegura:\n" + "\n".join(f"- {error}" for error in errores)
    return "Contraseña muy segura. ¡Perfecto!"


def main():
    print("Validador de correo y contraseñas")
    print("Ingrese su correo para validar. Deje vacío y presione Enter para salir.")

    while True:
        email = input("Email: ")
        contraseña = input("Contraseña: ")
        if email == "" and contraseña == "":
            print("Saliendo.")
            break
        
        resultado_e=validar_email(email)
        resultado = validar_contrasena(contraseña)
        print(resultado_e)
        print("-" * 40)
        print(resultado)
        print("-" * 40)


if __name__ == "__main__":
    main()