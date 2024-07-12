# Device Classification App

This is a Streamlit-based web application that classifies devices as either "Laptop" or "Mobile" using a pre-trained deep learning model.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Model](#model)
- [Contributing](#contributing)
- [License](#license)

## Overview

This application allows users to upload an image, which is then classified by a convolutional neural network (CNN) model saved as `device-classification.keras`. The model predicts whether the uploaded image is of a Laptop or a Mobile device.

## Features

- User-friendly interface for image upload.
- Real-time classification of uploaded images.
- Displays the uploaded image along with the classification result.

  
## Screenshot

![Device Classification App](https://github.com/ritigit7/Device-Prediction/blob/main/Screenshot%202024-07-12%20114447.png)

## Installation

To run this application locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/ritigit7/device-classification-app.git
    cd device-classification-app
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Ensure you have the model file**:
    Place the `device-classification.keras` model file in the project directory.

## Usage

To start the application, run the following command:
```bash
streamlit run app.py
