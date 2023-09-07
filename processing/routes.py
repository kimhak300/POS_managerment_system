import psutil

from processing import app, streamlit_app
from flask import request, jsonify
from processing.scrape import DomesticData, International
from processing.constant import psf
from flask import render_template
import streamlit as st
import os
import subprocess


@app.route('/')
@app.route('/home_page')
def home_page():
    return render_template("home.html")


# Initialize the response variable
response = {}

@app.route('/process_form', methods=['POST'])
def process_form():
    global response

    if 'download_button_domestic' in request.form:
        # Retrieve user input
        path = request.form.get('location')
        choice = request.form.get('category-domestic')  # Use 'category-download' for domestic data
        website = request.form.get('domestic-websites')
        if website == 'website1':
            try:
                DomesticData.GDP(path, choice).scrap_GDP_Choice()
                response = {'status': 'success', 'message': 'Data download successful!', 'dir:': path}
            except Exception as e:
                response = {'status': 'error', 'message': f'Error: {str(e)}'}
        else:
            try:
                DomesticData.NBC(path, choice).scrap_NBC_Choice()
                response = {'status': 'success', 'message': 'Data download successful!', 'dir:': path}
            except Exception as e:
                response = {'status': 'error', 'message': f'Error: {str(e)}'}

    if "download_button_international" in request.form:
        # Retrieve user input
        location = request.form.get('path-international')
        website = request.form.get('international-website')
        day = request.form.get('day')
        month = request.form.get('month')
        year = request.form.get('year')
        scrapping = International.Scraper(path=location, year=year, day=day, month=month)
        if website == 'website1':
            try:
                scrapping.opec_org()
                response = {'status': 'success', 'message': 'Data download successful!'}
            except Exception as e:
                response = {'status': 'error', 'message': f'Error: {str(e)}'}
        elif website == 'website2':
            scrapping.ExchangeRateIndonesia()
            try:
                response = {'status': 'success', 'message': 'Data download successful!'}
            except Exception as e:
                response = {'status': 'error', 'message': f'Error: {str(e)}'}
        elif website == 'website3':
            scrapping.thailand_exchange_rate()
            try:
                response = {'status': 'success', 'message': 'Data download successful!'}
            except Exception as e:
                response = {'status': 'error', 'message': f'Error: {str(e)}'}

    # Handle other form submissions or render the page as needed
    return render_template('home.html', response=response)


# Define the Streamlit process globally
streamlit_process = None
@app.route('/streamlit')
def streamlit_page():
    global streamlit_process  # Declare the variable as global

    # Check if a Streamlit process is already running
    if streamlit_process is None or not psutil.pid_exists(streamlit_process.pid):
        # Streamlit is not running, so start a new process
        streamlit_command = ["streamlit", "run", psf, "--server.headless", "true"]

        try:
            streamlit_process = subprocess.Popen(streamlit_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            out, err = streamlit_process.communicate()

            if streamlit_process.returncode != 0:
                print("Error running Streamlit app. Return code:", streamlit_process.returncode)
                print("Streamlit error output:", err)
            else:
                print("Streamlit output:", out)
        except Exception as e:
            print("Error:", e)
    else:
        print("Streamlit is already running")

    return render_template('streamlit.html')






