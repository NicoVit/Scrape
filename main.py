***CODE INCOMPLETE, FULL CODE AND OTHER FILES ARE PRIVATE. THIS IS FOR SAMPLING***


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
import time
import csv
import string
import sys
import random
import requests
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import urllib.request
from urllib.request import urlopen
from streamlit.components.v1 import html
import streamlit as st
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from io import BytesIO

if __name__ == '__main__':
    pass

def login_to_website(username, password, start, end):
    base_url = **PRIVATE**
    options = webdriver.ChromeOptions()
    ua = UserAgent()
    user_agent = ua.random
    options.add_argument(f'user-agent={user_agent}')
    options.add_argument("javascript.enabled")
    options.add_argument("--incognito")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-cache")
    options.add_argument("--start-maximized")
    options.add_experimental_option("debuggerAddress", "localhost:9999")
    service = Service(executable_path=r'/usr/bin/chromedriver')
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(base_url)
    driver.delete_all_cookies()
    wait = WebDriverWait(driver, 20)
    try:
        start_login_process(driver, wait, start, end)
    except TimeoutException:
        new_tab_script = "window.open('', '_blank');"
        driver.execute_script(new_tab_script)
        driver.switch_to.window(driver.window_handles[-1])
        driver.get(base_url)
        driver.delete_all_cookies()
        start_login_process()

def start_login_process(driver, wait, start, end):
    input_box = driver.find_element(By.XPATH, "//div[@class='ux-text-input-shell']//input[@type='text']")
    time.sleep(2)
    password_input_box = driver.find_element(By.XPATH, "//div[@id='password-container']//input[@type='password']")
    time.sleep(2)
    button = wait.until(EC.element_to_be_clickable((By.ID, 'submitBtn'))).click()
    time.sleep(5)
    button = wait.until(EC.element_to_be_clickable((By.ID, 'capsule-venture-0'))).click()
    time.sleep(5)
    element = driver.find_element(By.CSS_SELECTOR, 'div[data-aid="Metrics-OrdersTile-844cdVQ2d"]').click()
    time.sleep(5)
    button = driver.find_element(By.XPATH, '//a[@class="ux-button MetricsDeepDiveSidebar-button ux-button-primary" and contains(span,"Manage orders")]').click()
    view_results(driver, start, end)

def view_results(driver, start, end):
    wait = WebDriverWait(driver, 20)
    input_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Start"]')))
    input_element.send_keys(start)
    output_element = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Stop"]')
    output_element.send_keys(end)
    button = driver.find_element(By.ID, 'order-list-search-btn').click()
    auto_scroll(driver)

def auto_scroll(driver):
    rows = []
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            try:
                sort_data(driver, rows)
                click_next_page(driver)
            except Exception as e:
                print("Reached the last page.")
                break
        last_height = new_height
        new_rows = driver.find_elements(By.CSS_SELECTOR, '.flex-table-row.cursor-pointer.hoverable')
        rows += new_rows
    clean_links(driver, links)
    scrape_link(driver, clean)
    data = {
        'SKU/Quantity': sku_list,
        'Date': dates_list,
        'Payment Status': status_list,
        'Name': names,
        'Address': address,
        'Phone Number': phone_numbers,
        'Special Instructions': special_instructions_list,
        'Coupon Code': coupon_codes,
        'Bag Number': [''] * len(sku_list),
        'Delivery Order Number': [''] * len(sku_list)
    }
    df = pd.DataFrame(data)
    st.session_state.df = df
    st.session_state.page = 3

def click_next_page(driver):
    next_page_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//li[@class="page-item next "]//button[@aria-label="Go to next page"]'))
    )
    next_page_button.click()
    

def sort_data(driver, rows):
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    order_number_links = soup.select('a[data-ga="sale_click_order_number"]')
    for order_number_link in order_number_links:
        order_number_url = order_number_link.get('href')
        links.append(order_number_url)

def clean_links(driver, links):
    base_url = **PRIVATE**
    for link in links:
        full_url = base_url + link
        clean.append(full_url)

def scrape_link(driver, clean):
    for url in clean:
        driver.get(url)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        try:
            coupon_element = driver.find_element(By.XPATH, '//td[@class="item-total" and contains(text(), "Coupon")]')
            coupon_code = coupon_element.text.split("(")[-1].split(")")[0]
            coupon_codes.append(coupon_code)
        except NoSuchElementException:
            coupon_codes.append("No coupon codes found")
        temp_string = ""
        try:
            stock_items = driver.find_elements(By.CLASS_NAME, 'stock-item')
            for item in stock_items:
                sku_element = item.find_element(By.CLASS_NAME, 'item-sku')
                sku = sku_element.find_element(By.CLASS_NAME, 'item-option-value').text
                temp_string += str(sku) 
                temp_string += ": "
                try:
                    quantity_element = item.find_element(By.CLASS_NAME, 'item-quantity')
                    quantity_text = quantity_element.text
                    quantity = int(quantity_text.split('x')[1].strip())
                    temp_string += str(quantity)
                except NoSuchElementException:
                    quantity = 1
                    temp_string += str(quantity)
                temp_string += " "
            sku_list.append(temp_string)
        except NoSuchElementException:
            sku_list.append("No SKU found")
        try:
            special_instructions_header = driver.find_element(By.ID, 'special-instructions-header')
            if special_instructions_header.is_displayed():
                special_instructions = driver.find_element(By.CLASS_NAME, 'instruction-line').text
                special_instructions_list.append(special_instructions)
        except NoSuchElementException:
            special_instructions_list.append("No special instructions")
        try:
            phone_element = driver.find_element(By.XPATH, "//p[contains(@class, 'mb-0')]")
            phone = phone_element.text.strip()
            phone_numbers.append(phone)
        except NoSuchElementException:
            phone_numbers.append("No phone number provided")
        try:
            recipient_element = driver.find_element(By.CSS_SELECTOR, 'p.recipient-name strong')
            recipient_name = recipient_element.text.strip()
            names.append(recipient_name)
        except NoSuchElementException:
            names.append("Recipient name not found")
        try:
            street_element = driver.find_element(By.CSS_SELECTOR, 'div.user-address p:nth-child(1)')
            city_state_zip_element = driver.find_element(By.CSS_SELECTOR, 'div.user-address p:nth-child(2)')
            address.append(street_element.text.strip() + ", " + city_state_zip_element.text.strip())
        except NoSuchElementException:
            address.append("No address found")
        statuses = driver.find_elements(By.CSS_SELECTOR, '.status-paid, .status-unpaid')
        for status in statuses:
            status_text = status.text.strip().lower()
            status_list.append(status_text)
            if 'paid' in status_text:
                dates = driver.find_elements(By.CSS_SELECTOR, '.order-history-date')
                for date_element in dates:
                    date_text = date_element.text.strip()
                    dates_list.append(date_text)
            else:
                dates_list.append("Order not fulfilled")
    

links = []
clean = []
status_list = []
dates_list = []
names = []
address = []
phone_numbers = []
special_instructions_list = []
sku_list = []
coupon_codes = []
st.title(**PRIVATE**)
if "page" not in st.session_state:
    st.session_state.page = 1
if st.session_state.page == 1:
    st.header("Enter your information")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if "loading" not in st.session_state:
        st.session_state.loading = False
    if st.button("Login"):
        st.session_state.email = email
        st.session_state.password = password
        st.session_state.page = 2
if st.session_state.page == 2:
    st.header("Select Dates to Search:")
    start_date = st.text_input("Start Date")
    end_date = st.text_input("End Date")
    if st.button("Start the Search:"):
        st.session_state.start_date = start_date
        st.session_state.end_date = end_date
        login_to_website(st.session_state.email, st.session_state.password, st.session_state.start_date, st.session_state.end_date)
if st.session_state.page == 3:
    st.header("View Data:")
    st.write(st.session_state.df)
    def get_dataframe_download_link():
        excel_data = BytesIO()
        with pd.ExcelWriter(excel_data, engine='xlsxwriter') as writer:
            st.session_state.df.to_excel(writer, index=False)
        excel_data.seek(0)
        return excel_data.read()

    dataframe_link = get_dataframe_download_link()
    st.download_button(label='Download DataFrame', data=dataframe_link, file_name='raw_dataframe.xlsx', mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

        
