from processing import app
from flask import request, jsonify
from processing.scrape import DomesticData, International
from flask import render_template

@app.route('/')
@app.route('/home_page')
def home_page():
    return render_template("home.html")


@app.route('/process_form', methods=['POST'])
def process_form():

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

        return jsonify(response)  # Return JSON response

    if "download_button_international" in request.form:
        # Retrieve user input
        location = request.form.get('path-international')
        website = request.form.get('international-website')
        day = request.form.get('day')
        month = request.form.get('month')
        year = request.form.get('year')
        scrapping = International.Scraper(path=location, year= year, day= day, month=month)
        if website == 'website1':
            try:
                scrapping.opec_org()
                response = {'status': 'success', 'message': 'Data download successful!'}
            except Exception as e:
                response = {'status': 'error', 'message': f'Error: {str(e)}'}
        else:
            scrapping.ExchangeRateIndonesia()
            try:
                response = {'status': 'success', 'message': 'Data download successful!'}
            except Exception as e:
                response = {'status': 'error', 'message': f'Error: {str(e)}'}

        return jsonify(response)  # Return JSON response

    # Handle other form submissions or render the page as needed
    return render_template('home.html')



