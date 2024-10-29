import flet as ft
import re
from validador import validar_expresion2


def main(page: ft.Page):
    # se define un diseño responsivo
    page.adaptive = True
    # Se añade el scroll, en caso de que haya muchos elementos para la pantalla
    page.scroll = ft.ScrollMode.ADAPTIVE

    page.title = "Proyecto final"

    # Se crea un AppBar que funciona como barra de título para el programa
    page.appbar = ft.AppBar(
        title=ft.Text("Validador de expresiones regulares"),
        center_title=True,
        bgcolor=ft.colors.BLUE,
    )

    # Contenedor para los elementos que cambiarán
    content = ft.Column(scroll=ft.ScrollMode.ALWAYS)

    # ------------------------------
    # Elementos de la interfaz
    # ----------------------------------
    # Elementos de la sección de validar autómatas
    presentacion = ft.Text("Aquí puedes validar una cadena")
    informacion = ft.Text("Contenido adicional para validar cadena.")
    recomendacion = ft.Text("Se recomienda ingresar las siguientes expresiones", theme_style=ft.TextThemeStyle.LABEL_LARGE)

    # Expresiones
    expresion1 = "^\d{10}$"
    expresion1_explicacion = "Se valida una cadena de exactamente 10 dígitos"
    expresion2 = "^[a-zA-Z]+$"
    expresion2_explicacion = "Se valida una cadena de solo letras, el + indica que debe haber al menos una letra"
    expresion3 = "^a{2,}$ "
    expresion3_explicacion = "Se valida una cadena donde haya al menos dos letras a"

    texto_expresiones_recomendadas = (
        f"{expresion1}\n"
        f"{expresion1_explicacion}\n\n"
        f"{expresion2}\n"
        f"{expresion2_explicacion}\n\n"
        f"{expresion3}\n"
        f"{expresion3_explicacion}"
    )

    extension_recomendacion = ft.Text(texto_expresiones_recomendadas, theme_style=ft.TextThemeStyle.LABEL_LARGE)

    text_field_expresion = ft.TextField(label="Ingrese la expresión regular")
    text_field_cadenas = ft.TextField(label="Ingrese la cadena a validar")
    # la idea es tener un text area a futuro
    # text_field_cadenas = ft.TextField(label="Ingrese las cadenas a validar", multiline=True, min_lines=1)

    resultado = ft.Text("Resultado de la validación", theme_style=ft.TextThemeStyle.TITLE_MEDIUM)

    # ------------------------------------------
    # Elementos de la sección de ayuda
    texto_instrucciones = ft.Text("¿Qué debo ingresar?",
                                  theme_style=ft.TextThemeStyle.TITLE_LARGE,
                                  weight=ft.FontWeight.BOLD
                                  )
    string_explicacion = ("Se deben ingresar expresiones regulares, con el fin de validar cadenas para verificar"
                      " si corresponden a la expresión ingresada o no. Una expresión regular está conformada "
                      "por los siguientes elementos")
    texto_explicacion = ft.Text(string_explicacion,
                            theme_style=ft.TextThemeStyle.LABEL_LARGE)

    # Reglas de los caracteres
    elemento_1 = "^, que marca el inicio de la cadena"
    elemento_2 = "$, que marca el final de la cadena"
    elemento_3 = "a-z, para las letras minúsculas desde a hasta z"
    elemento_4 = "A-Z, para las letras mayúsculas desde A hasta Z"
    elemento_5 = ("^, también funciona como negación, por ejemplo ^abc,"
                  " se refiere a cualquier letra distinta a la a, b y c")
    elemento_6 = "d, para referirse a cualquier dígito"
    elemento_7 = "w, para referirse a los caracteres alfanumericos (letras, números y guión bajo)"
    elemento_8 = "s, para referirse a un espacio en blanco"

    texto_caracteres = (
        f"{elemento_1}\n"
        f"{elemento_2}\n"
        f"{elemento_3}\n"
        f"{elemento_4}\n"
        f"{elemento_5}\n"
        f"{elemento_6}\n"
        f"{elemento_7}\n"
        f"{elemento_8}"
    )
    titulo_caracteres = ft.Text("Reglas de los caracteres",
                                theme_style=ft.TextThemeStyle.TITLE_MEDIUM,
                                weight=ft.FontWeight.BOLD
                                )
    texto_base_caracteres = ft.Text(texto_caracteres, theme_style=ft.TextThemeStyle.LABEL_LARGE)

    # Reglas de los cuantificadores
    cuantificador1 = "*, que coincide con 0 o más repeticiones del elemento anterior"
    cuantificador2 = "+, que coincide con 1 o más repeticiones del elemento anterior"
    cuantificador3 = "?, que coincide con 0 o 1 repetición del elemento anterior"
    cuantificador4 = ("{n},  que coincide exactamente con n repeticiones del elemento anterior,"
                      "por ejemplo a{3} para 3 aes o aaa")
    cuantificador5 = "{n,}, que coincide con al menos n repeticiones del elemento anterior"
    cuantificador6 = "{n,m}, que coincide con al menos n y como máximo m repeticiones"

    texto_cuantificadores = (
        f"{cuantificador1}\n"
        f"{cuantificador2}\n"
        f"{cuantificador3}\n"
        f"{cuantificador4}\n"
        f"{cuantificador5}\n"
        f"{cuantificador6}"
    )

    titulo_cuantificadores = ft.Text("Reglas de los cuantificadores",
                                     theme_style=ft.TextThemeStyle.TITLE_MEDIUM,
                                     weight=ft.FontWeight.BOLD
                                     )
    texto_base_cuantificadores = ft.Text(texto_cuantificadores, theme_style=ft.TextThemeStyle.LABEL_LARGE)

    # Reglas de grupos
    grupo1 = "Los paréntesis ( ) se utilizan para agrupar elementos y tratarlos como una sola unidad"
    grupo2 = "Por ejemplo, (abc) solo corresponde a la secuencia exacta abc"
    grupo3 = "Por otro lado, usando | se tiene que: (ab|cd): coincide con ab o cd"

    texto_grupos = (
        f"{grupo1}\n"
        f"{grupo2}\n"
        f"{grupo3}"
    )

    titulo_grupos = ft.Text("Reglas de los grupos",
                            theme_style=ft.TextThemeStyle.TITLE_MEDIUM,
                            weight=ft.FontWeight.BOLD
                            )
    texto_base_grupos = ft.Text(texto_grupos, theme_style=ft.TextThemeStyle.LABEL_LARGE)

    # Ejemplos
    ejemplo1 = "^\d{10}$"
    ejemplo1_explicacion = "Se valida una cadena de exactamente 10 dígitos"
    ejemplo2 = "^[a-zA-Z]+$"
    ejemplo2_explicacion = "Se valida una cadena de solo letras, el + indica que debe haber al menos una letra"
    ejemplo3 = "^a{2,}$ "
    ejemplo3_explicacion = "Se valida una cadena donde haya al menos dos letras a"

    texto_ejemplos = (
        f"{ejemplo1}\n"
        f"{ejemplo1_explicacion}\n\n"
        f"{ejemplo2}\n"
        f"{ejemplo2_explicacion}\n\n"
        f"{ejemplo3}\n"
        f"{ejemplo3_explicacion}"
    )

    titulo_ejemplos = ft.Text("Ejemplos de expresiones regulares",
                            theme_style=ft.TextThemeStyle.TITLE_MEDIUM,
                            weight=ft.FontWeight.BOLD
                            )
    texto_base_ejemplos = ft.Text("Se tienen las siguientes expresiones", theme_style=ft.TextThemeStyle.LABEL_LARGE)

    texto_base2_ejemplos = ft.Text(texto_ejemplos, theme_style=ft.TextThemeStyle.LABEL_LARGE)
    # ---------------------------------------

    # Funciones que crean el contenido de cada pantalla
    # se puede tomar cada función como una pantalla distinta
    def explore_content():
        return ft.Column([
            presentacion,
            informacion,
            recomendacion,
            extension_recomendacion,
            # Se crea un textField para la expresión regular
            text_field_expresion,
            # Se crea un textField con múltiples líneas para ingresar las cadenas
            text_field_cadenas,

            # Se crea el botón para validar la expresión
            ft.ElevatedButton(
                "Validar expresión",
                icon="TEXT_INCREASE_ROUNDED",
                icon_color="green400",
                on_click=validar_expresion
            ),

            # Se crea el texto de resultado
            resultado
        ])

    def commute_content():
        return ft.Column([
            ft.Text("Aquí puedes generar un autómata"),
            ft.Text("Contenido adicional para generar autómata.")
        ])

    def bookmark_content():
        return ft.Column([
            ft.Text("Aquí puedes leer información de la aplicación"),
            ft.Text("Contenido adicional del manual de usuario"),
            texto_instrucciones,
            texto_explicacion,
            titulo_caracteres,
            texto_base_caracteres,
            titulo_cuantificadores,
            texto_base_cuantificadores,
            titulo_grupos,
            texto_base_grupos,
            titulo_ejemplos,
            texto_base_ejemplos,
            texto_base2_ejemplos
        ])

    # -------------------------------------------------------------------------

    # Función para actualizar el contenido
    def on_nav_change(e):
        content.controls.clear()  # Limpiar el contenido actual

        # Cambiar el contenido según la selección
        if e.control.selected_index == 0:
            content.controls.append(explore_content())
        elif e.control.selected_index == 1:
            content.controls.append(commute_content())
        elif e.control.selected_index == 2:
            content.controls.append(bookmark_content())

        content.update()

    # Definir el NavigationBar con el evento on_change
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.icons.CHECK_CIRCLE_SHARP, label="Validar cadena"),
            ft.NavigationBarDestination(icon=ft.icons.BROKEN_IMAGE_OUTLINED, label="Generar autómata"),
            ft.NavigationBarDestination(
                icon=ft.icons.QUESTION_MARK,
                label="Manual de usuario",
            ),
        ],
        on_change=on_nav_change,
    )

    # -------------------------------------------------------------------
    # Funciones de la lógica
    # --------------------------------------------------------------------

    # Función para validar la cadena
    def validar_expresion_regular(expresion, cadena):
        try:
            # Compilar la expresión regular
            patron = re.compile(expresion)
            # Validar la cadena
            return patron.match(cadena) is not None
        except re.error:
            return False  # La expresión no es válida

    def validar_expresion(e):
        resultado.value = "Expresión validada correctamente"
        resultado.update()

        expresion_entrada = text_field_expresion.value
        cadena_entrada = text_field_cadenas.value

        if validar_expresion_regular(expresion_entrada, cadena_entrada):
            resultado.value = "La expresión es válida"
        else:
            resultado.value = "La expresión no es válida"
        resultado.update()
        page.update()

    # --------------------------------------------
    # Agregar el contenedor al layout de la página
    page.add(content)


ft.app(main)
