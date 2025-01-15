from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

# Ruta al WebDriver de Edge
driver_path = "C:/Driver_IE/msedgedriver.exe"  # Cambia esta ruta si el archivo está en otro lugar

# Configurar Edge
options = webdriver.EdgeOptions()
options.use_chromium = True  # Asegura que use el núcleo Chromium

# Inicia el navegador
driver = webdriver.Edge(executable_path=driver_path, options=options)

try:
    # Abre la página web
    url = "https://nevalia.barceloviveahora.com/login"
    driver.get(url)

    # Maximiza la ventana
    driver.maximize_window()
    time.sleep(1)  # Esperar para asegurar que la página carga completamente

    # Encuentra los campos de entrada y el botón
    email_input = driver.find_element(By.NAME, "email")  # Ajusta el selector si es necesario
    password_input = driver.find_element(By.NAME, "password")  # Ajusta el selector si es necesario

    # Escribe las credenciales
    email_input.send_keys("example@gmail.com") #Aqui poner correo
    password_input.send_keys("*****") #Aqui poner contraseña

    # Hacer clic en el botón de inicio de sesión
    login_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Entrar')]")
    login_button.click()

    # Espera unos segundos para cargar la siguiente página
    time.sleep(2)
    
    # Aceptar cookies
    try:
        accept_cookies_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Aceptar')]"))
        )
        accept_cookies_button.click()
        print("Cookies aceptadas.")
    except Exception:
        print("No se encontró el banner de cookies o ya fue aceptado.")

    # Hacer scroll hacia el botón "JUGAR"
    play_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "play-again-button"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", play_button)  # Desplazar al botón
    time.sleep(1)  # Esperar un momento después del scroll

    # Hacer clic en el botón "JUGAR"
    play_button.click()
    
    # Bucle infinito
    while True:
        time.sleep(2)  # Esperar antes de repetir el bucle
        
         # Esperar a que aparezca el gameBoard
        print("Esperando a que aparezca el 'gameBoard'...")
        game_board = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "gameBoard"))
        )

        # Realizar clic en el centro del gameBoard
        print("Clic en el centro del 'gameBoard'...")
        actions = ActionChains(driver)
        actions.move_to_element(game_board).click().perform()
        jugadas+=1
        time.sleep(2)  # Esperar antes de repetir el bucle
        
        
        
        
        # Hacer scroll hacia el botón "JUGAR"
        play_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "play-again-button"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", play_button)  # Desplazar al botón
        time.sleep(2)  # Esperar un momento después del scroll

        # Hacer clic en el botón "JUGAR"
        play_button.click()
        
        
        # Hacer scroll hacia el botón "JUGAR"
        play_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "play-again-button"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", play_button)  # Desplazar al botón
        time.sleep(2)  # Esperar un momento después del scroll

        # Hacer clic en el botón "JUGAR"
        play_button.click()
        

        # Llegará al resultado del juego, y el bucle repetirá todo desde el botón "JUGAR OTRA VEZ"


    print("El botón 'JUGAR' fue clicado exitosamente.")

except Exception as e:
    print("jugadas" + jugadas)
    print("Ocurrió un error:", str(e))

# El navegador permanecerá abierto
