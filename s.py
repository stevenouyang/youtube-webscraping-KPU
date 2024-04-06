import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#! vs__search (input)
#! vs__dropdown-option 

# ? Save Image
def save_image(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        
        with open(save_path, 'wb') as f:
            f.write(response.content)
            print("Gambar Berhasil disimpan", save_path)
            
    else:
        print("gambar gagal disimpan")

# ? Get image url
def get_image_url():
    element = driver.find_elements(By.XPATH, '//div[@class="col-md-4"]')
    if len(element) >= 2:
        image_element_url = element[1].find_element(By.TAG_NAME, 'img')
        return image_element_url.get_attribute('src')

# ? Untuk Cari dropdown option
def get_dropdown_option_tps():
    input_element = driver.find_element(By.XPATH, '(//input[@class="vs__search"])[7]')
    input_element.click()
    time.sleep(1)
    
    options = driver.find_elements(By.CSS_SELECTOR, '.vs__dropdown-option')
    print(len(options))
    
    data = [option.text for option in options]
    return data

def get_dropdown_option_kelurahan():
    input_element = driver.find_element(By.XPATH, '(//input[@class="vs__search"])[6]')
    input_element.click()
    time.sleep(1)
    
    options = driver.find_elements(By.CSS_SELECTOR, '.vs__dropdown-option')
    print(len(options))
    
    data = [option.text for option in options]
    return data


# ? Untuk klik dropdown option dan masukkan value lalu di enter
def click_and_input_tps(option):
    input_element = driver.find_element(By.XPATH, '(//input[@class="vs__search"])[7]')
    input_element.clear()
    
    input_element.send_keys(option)
    input_element.send_keys(Keys.RETURN)
    
    time.sleep(1)

def click_and_input_kelurahan(option):
    input_element = driver.find_element(By.XPATH, '(//input[@class="vs__search"])[6]')
    input_element.clear()
    
    input_element.send_keys(option)
    input_element.send_keys(Keys.RETURN)
    
    time.sleep(1)

if __name__ == "__main__":
    starting_url= ""
    driver = webdriver.Chrome()
    driver.get(starting_url)

    #! PROVINSI-KABUPATEN-KECAMATAN-KELURAHAN-TPS 000
    
    provinsi = "JAKARTA"
    kabupaten = "ADM. KEP. SERIBU"
    kecamatan = "KEPULAUAN SERIBU SELATAN"
    
    possible_kelurahan = get_dropdown_option_kelurahan()
    
    for kelurahan in possible_kelurahan:
        click_and_input_kelurahan(kelurahan)
        possible_tps = get_dropdown_option_tps()
    
        for tps in possible_tps:
            click_and_input_tps(tps)
            image = get_image_url()
            if image:
                save_path = f"hasil/{provinsi}-{kabupaten}-{kecamatan}-{kelurahan}-{tps}.jpg"
                save_image(image, save_path)
        
    driver.quit()