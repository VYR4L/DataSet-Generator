from playwright.sync_api import sync_playwright
from time import sleep


def download_images(url, output_dir):
    downloads = 0
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(accept_downloads=True)

        # Initialize the page and navigate to the URL
        page = context.new_page()
        page.goto(url)

        # Move the mouser to the center of the page
        # This is necessary 'cause the page doesn't load the images
        # until the mouse is over it
        page.mouse.move(500, 500)

        calssification_button = page.get_by_text("Select Emotion")
        calssification_button.select_option("Neutral")
        sleep(2)

        while downloads < 3000:
            for i in range(8):  # IDs A0 - A7
                image_id = f"#A{i}"  # Seleciona o ID da imagem
                image_element = page.locator(image_id)
                
                # Clica na imagem para abrir as opções de download
                image_element.click()
                sleep(1)
                
                # Clica no botão de download
                download_button = page.get_by_text("Download 512 x 512")
                with page.expect_download() as download_info:
                    download_button.click()  # Inicia o download
                download = download_info.value  # Captura o evento de download
                
                # Salva o arquivo baixado no diretório especificado
                download.save_as(output_dir / f"face_{downloads}.jpg")
                downloads += 1

                # Clica no botão de close para fechar o menu
                close_button = page.locator(".closex")
                close_button.click()
                sleep(0.5)

            # Clica no botão de refresh para gerar novas imagens
            refresh_button = page.locator(".reloadbtnx")
            refresh_button.click()
            sleep(2)

            if downloads >= 3000:
                print("Download complete!")
                break

