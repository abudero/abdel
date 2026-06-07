import re

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
    print("Validador de contraseñas")
    print("Ingrese contraseñas para validar. Deje vacío y presione Enter para salir.")

    while True:
        contraseña = input("Contraseña: ")
        if contraseña == "":
            print("Saliendo.")
            break

        resultado = validar_contrasena(contraseña)
        print(resultado)
        print("-" * 40)


if __name__ == "__main__":
    main()

