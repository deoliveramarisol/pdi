import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Lista de números de teléfono
numeros_telefono = ['+541130893476', '+541170547811', '+541173626082']

# Función para abrir una nueva pestaña con Selenium
def abrir_nueva_pestana(driver):
    driver.execute_script("window.open('');")

# Función para enviar mensajes automáticos
def enviar_mensajes_automaticos():
    try:
        print("Iniciando envío de mensajes automáticos...")

        # Configurar el WebDriver
        with webdriver.Chrome() as driver:  # Esto cerrará automáticamente el navegador al salir del bloque with
            driver.get("https://web.whatsapp.com/")
            WebDriverWait(driver, 20).until(EC.title_contains("WhatsApp"))  # Espera a que la página cargue completamente

            # Abre nuevas pestañas según la cantidad de números
            for _ in range(len(numeros_telefono) - 1):
                abrir_nueva_pestana(driver)

            # Cambiar de pestaña para cada número
            for i, numero in enumerate(numeros_telefono):
                try:
                    if i < len(driver.window_handles):
                        driver.switch_to.window(driver.window_handles[i])

                        # Mensajes a enviar
                        mensajes = entrada_mensaje.get()

                        # Construye la URL de WhatsApp
                        url_whatsapp = f'https://web.whatsapp.com/send?phone={numero}&text={mensajes}'
                        driver.get(url_whatsapp)

                        # Espera a que aparezca el campo de entrada de texto
                        campo_texto = WebDriverWait(driver, 20).until(
                            EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-tab="1"]'))
                        )

                        # Envía el mensaje
                        campo_texto.send_keys(mensajes)
                        campo_texto.send_keys(Keys.RETURN)

                        # Espera a que se envíe el mensaje
                        WebDriverWait(driver, 20).until(
                            EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'span[data-icon="msg-time"]'), 'ahora')
                        )
                    else:
                        print(f"La ventana {i} ya ha sido cerrada.")
                except Exception as e:
                    print(f"Se produjo un error: {e}")

    except Exception as e:
        print(f"Se produjo un error: {e}")

# Crear la ventana principal
root = tk.Tk()
root.title("Enviar Mensajes Automáticos de WhatsApp")

# Etiqueta y entrada para el mensaje
etiqueta_mensaje = tk.Label(root, text="Mensaje:")
etiqueta_mensaje.pack()
entrada_mensaje = tk.Entry(root)
entrada_mensaje.pack()

# Botón para enviar mensajes automáticos
boton_enviar = tk.Button(root, text="Enviar Mensajes Automáticos", command=enviar_mensajes_automaticos)
boton_enviar.pack()

# Iniciar el bucle principal
root.mainloop()
