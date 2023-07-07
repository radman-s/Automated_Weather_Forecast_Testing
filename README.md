# Weather Verification Script

This script combines API requests and web element assertions to verify weather forecast details for a selected location.

## Description

The Weather Verification Script is a Python script that utilizes API requests to retrieve weather forecast data from the OpenWeatherMap API. It then uses Selenium WebDriver to locate and extract weather information from web elements on a weather website. The script compares the API data with the data displayed on the website, asserting that the information matches the expected values.

## Features

- Retrieves weather forecast data from the OpenWeatherMap API
- Utilizes Selenium WebDriver to locate and extract weather information from web elements
- Verifies temperature, feels like, humidity, visibility, wind speed, pressure, and other weather attributes
- Provides assertions to ensure the accuracy of weather data between the API and website

## Prerequisites

- Python 3.x installed
- Selenium WebDriver library installed (`pip install selenium`)
- Chrome WebDriver executable installed and in the system PATH
- Access to the OpenWeatherMap API with a valid API key

## Usage

1. Clone the repository or download the script file to your local machine.
2. Install the required dependencies by running `pip install selenium`.
3. Set up the Chrome WebDriver by downloading the appropriate version for your Chrome browser and ensuring it is in the system PATH.
4. Open the script file in a text editor and modify any necessary configuration settings, such as the API key.
5. Run the script using Python: `python main_script.py`.

## Configuration

The script includes various configuration options that can be modified based on your requirements:

- API key: Replace the placeholder API key with your own OpenWeatherMap API key.
- Tolerance: Adjust the tolerance level for comparing weather values between the API and website.
- Verification options: Enable or disable specific weather attribute verifications as needed.

## Notes

- The script assumes a specific structure of the weather website's web elements. Modify the web element locators and extraction logic as necessary to match your website's structure.
- This script serves as a basic example and can be expanded upon or customized to fit your specific needs.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
