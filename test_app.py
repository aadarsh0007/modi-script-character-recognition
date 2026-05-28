<<<<<<< HEAD
import requests
import os
from PIL import Image
import io

# Base URL of the running Flask app
BASE_URL = 'http://localhost:5000'

def test_login():
    print("Testing login page...")
    response = requests.get(f'{BASE_URL}/login')
    if response.status_code == 200:
        print("✓ Login page loads successfully")
    else:
        print(f"✗ Login page failed: {response.status_code}")

def test_register():
    print("Testing register page...")
    response = requests.get(f'{BASE_URL}/register')
    if response.status_code == 200:
        print("✓ Register page loads successfully")
    else:
        print(f"✗ Register page failed: {response.status_code}")

def test_forgot_password():
    print("Testing forgot password page...")
    response = requests.get(f'{BASE_URL}/forgot')
    if response.status_code == 200:
        print("✓ Forgot password page loads successfully")
    else:
        print(f"✗ Forgot password page failed: {response.status_code}")

def test_home_redirect():
    print("Testing home redirect...")
    response = requests.get(f'{BASE_URL}/', allow_redirects=False)
    if response.status_code == 302 and 'login' in response.headers.get('Location', ''):
        print("✓ Root redirects to login successfully")
    else:
        print(f"✗ Root redirect failed: {response.status_code}")

def test_image_upload_page():
    print("Testing image upload page...")
    # First, we need to login to access the image page
    session = requests.Session()
    # Try to login with valid credentials from database
    login_data = {'email': 'admin@gov.in', 'password': '1234'}  # Correct password from database
    response = session.post(f'{BASE_URL}/login', data=login_data, allow_redirects=False)
    if response.status_code != 302 and 'Invalid Credentials' in response.text:
        print("✗ Cannot login for testing image upload (invalid credentials)")
        return

    response = session.get(f'{BASE_URL}/image')
    if response.status_code == 200:
        print("✓ Image upload page loads successfully")
    else:
        print(f"✗ Image upload page failed: {response.status_code}")

def test_database_operations():
    print("Testing database operations...")
    import sqlite3
    try:
        conn = sqlite3.connect('mydatabase.db')
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        print(f"✓ Database tables: {[t[0] for t in tables]}")
        if 'Users' in [t[0] for t in tables]:
            cursor.execute("SELECT COUNT(*) FROM Users;")
            count = cursor.fetchone()[0]
            print(f"✓ Users table has {count} records")
        conn.close()
    except Exception as e:
        print(f"✗ Database test failed: {e}")

def test_model_loading():
    print("Testing model loading...")
    try:
        import tensorflow as tf
        model = tf.keras.layers.TFSMLayer("trained_model/MODI_CHR_REC", call_endpoint='serving_default')
        print("✓ TensorFlow model loads successfully")
    except Exception as e:
        print(f"✗ Model loading failed: {e}")

def test_prediction_function():
    print("Testing prediction function...")
    try:
        from utils import predict_img
        result, confidence = predict_img('static/img/test.jpg')
        print(f"✓ Prediction successful: {result}")
        print(f"✓ Confidence: {confidence}")
    except Exception as e:
        print(f"✗ Prediction test failed: {e}")

if __name__ == '__main__':
    print("Starting comprehensive testing of MODI Script Recognition App...\n")

    test_login()
    test_register()
    test_forgot_password()
    test_home_redirect()
    test_image_upload_page()
    test_database_operations()
    test_model_loading()
    test_prediction_function()

    print("\nTesting completed!")
=======
import requests
import os
from PIL import Image
import io

# Base URL of the running Flask app
BASE_URL = 'http://localhost:5000'

def test_login():
    print("Testing login page...")
    response = requests.get(f'{BASE_URL}/login')
    if response.status_code == 200:
        print("✓ Login page loads successfully")
    else:
        print(f"✗ Login page failed: {response.status_code}")

def test_register():
    print("Testing register page...")
    response = requests.get(f'{BASE_URL}/register')
    if response.status_code == 200:
        print("✓ Register page loads successfully")
    else:
        print(f"✗ Register page failed: {response.status_code}")

def test_forgot_password():
    print("Testing forgot password page...")
    response = requests.get(f'{BASE_URL}/forgot')
    if response.status_code == 200:
        print("✓ Forgot password page loads successfully")
    else:
        print(f"✗ Forgot password page failed: {response.status_code}")

def test_home_redirect():
    print("Testing home redirect...")
    response = requests.get(f'{BASE_URL}/', allow_redirects=False)
    if response.status_code == 302 and 'login' in response.headers.get('Location', ''):
        print("✓ Root redirects to login successfully")
    else:
        print(f"✗ Root redirect failed: {response.status_code}")

def test_image_upload_page():
    print("Testing image upload page...")
    # First, we need to login to access the image page
    session = requests.Session()
    # Try to login with valid credentials from database
    login_data = {'email': 'admin@gov.in', 'password': '1234'}  # Correct password from database
    response = session.post(f'{BASE_URL}/login', data=login_data, allow_redirects=False)
    if response.status_code != 302 and 'Invalid Credentials' in response.text:
        print("✗ Cannot login for testing image upload (invalid credentials)")
        return

    response = session.get(f'{BASE_URL}/image')
    if response.status_code == 200:
        print("✓ Image upload page loads successfully")
    else:
        print(f"✗ Image upload page failed: {response.status_code}")

def test_database_operations():
    print("Testing database operations...")
    import sqlite3
    try:
        conn = sqlite3.connect('mydatabase.db')
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        print(f"✓ Database tables: {[t[0] for t in tables]}")
        if 'Users' in [t[0] for t in tables]:
            cursor.execute("SELECT COUNT(*) FROM Users;")
            count = cursor.fetchone()[0]
            print(f"✓ Users table has {count} records")
        conn.close()
    except Exception as e:
        print(f"✗ Database test failed: {e}")

def test_model_loading():
    print("Testing model loading...")
    try:
        import tensorflow as tf
        model = tf.keras.layers.TFSMLayer("trained_model/MODI_CHR_REC", call_endpoint='serving_default')
        print("✓ TensorFlow model loads successfully")
    except Exception as e:
        print(f"✗ Model loading failed: {e}")

def test_prediction_function():
    print("Testing prediction function...")
    try:
        from utils import predict_img
        result, confidence = predict_img('static/img/test.jpg')
        print(f"✓ Prediction successful: {result}")
        print(f"✓ Confidence: {confidence}")
    except Exception as e:
        print(f"✗ Prediction test failed: {e}")

if __name__ == '__main__':
    print("Starting comprehensive testing of MODI Script Recognition App...\n")

    test_login()
    test_register()
    test_forgot_password()
    test_home_redirect()
    test_image_upload_page()
    test_database_operations()
    test_model_loading()
    test_prediction_function()

    print("\nTesting completed!")
>>>>>>> b5b5514d63ce41f838d6b481a00ba2b4df5a3c98
