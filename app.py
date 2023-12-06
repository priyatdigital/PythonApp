import os, requests
from flask import Flask, jsonify

import psycopg2
from psycopg2 import sql
from urllib.parse import urlparse
import socks
import socket
# from urlparse import urlparse

app = Flask(__name__)

proxyDict = {
              "http"  : 'https://r09cndoizux678:44m6nmtadw9bg10eowfxi45cyrbyku@us-east-shield-04.quotaguard.com:9294',
              "https" : 'https://r09cndoizux678:44m6nmtadw9bg10eowfxi45cyrbyku@us-east-shield-04.quotaguard.com:9294'
 }

 # Extract proxy connection details from env variable
proxy = urlparse('https://r09cndoizux678:44m6nmtadw9bg10eowfxi45cyrbyku@us-east-shield-04.quotaguard.com:9294')

@app.route('/')
def hello():
    # return 'Hello from Python!'
    r = requests.get('https://www.google.com', proxies=proxyDict)
    # r = requests.get('https://www.google.com')
    return r.text

def get_public_ip():
    try:
        # Use a service that echoes the client's IP address
        response = requests.get('https://api64.ipify.org?format=json')
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response and extract the IP address
            ip_address = response.json()['ip']
            return ip_address
        else:
            print(f"Error: Unable to fetch IP address. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")

    # Get and print the public IP address
    my_ip = get_public_ip()
    print(f"My public IP address is: {my_ip}")

@app.route('/dbconnect')
def connect():


    # Specify the path to the PostgreSQL certificate file
    certificate_path = '/app/postgresql.crt'
    key_path = '/app/postgresql.key'
    # Open the file and read the first line
    try:
        with open(certificate_path, 'r') as file:
            first_line = file.readline().strip()
            print(f"The first line of {certificate_path} is: {first_line}")
    except FileNotFoundError:
        print(f"File {certificate_path} not found.")
    except Exception as e:
        print(f"Error reading {certificate_path}: {e}")

    try:
        with open(key_path, 'r') as file:
            first_line = file.readline().strip()
            print(f"The first line of {key_path} is: {first_line}")
    except FileNotFoundError:
        print(f"File {key_path} not found.")
    except Exception as e:
        print(f"Error reading {key_path}: {e}")



    script_dir = os.path.dirname(os.path.realpath('postgresql.crt'))
    print('script path: ', script_dir)
    print("Current working directory:", os.getcwd())
    my_ip = get_public_ip()
    print(f"My public IP address is: {my_ip}")
    # Parse the database URL
    db_url = "postgres://ucrol25emqd2ch:p31d791a3fe8bcb5b5102d7b8b43f08ca70ee2cc9d7943c23b4db6b110324346e@ec2-52-2-248-148.compute-1.amazonaws.com:5432/d2r45oj3jf7gs7"
    url = urlparse(db_url)
    # Set up the proxy settings
    print(proxyDict)
    proxy_host = proxyDict['http']
    # proxy_ips = ['54.173.229.200', '54.175.230.252']
    proxy_ips = ['54.160.232.145', '44.215.229.88']
    proxy_port = 1080
    proxy_type = socks.SOCKS5  # Change this based on your proxy type
    print('proxy type')
    selected_proxy_ip = proxy_ips[0]
    # Set up the connection parameters
    print('proxy type 2')
    # conn_params = {
    #     'database': url.path[1:],
    #     'user': url.username,
    #     'password': url.password,
    #     'host': url.hostname,
    #     'port': url.port,
    #     'sslmode': 'disable',  # Use 'require' to enable SSL
    #     'sslcert': os.getcwd() + '/postgresql.crt',  # Path to client certificate file
    #     'sslkey': os.getcwd() + '/postgresql.key'  # Pat
    # }

    print('proxy type 3')
    # Set up the proxy
    # socks.set_default_proxy(proxy_type, addr=proxy_host)
    # socket.socket = socks.socksocket
    print('proxy type 4')
    # Connect to the database via proxy

    # Fixie Socks credentials and server information
    fixie_socks_host = "speedway.usefixie.com"
    fixie_socks_port = 1080  # The port number
    fixie_socks_user = "fixie"
    fixie_socks_pass = "k2KJ04rPQQ047n8"

    # Set up the SOCKS proxy
    socks.set_default_proxy(socks.SOCKS5, fixie_socks_host, fixie_socks_port, False, fixie_socks_user, fixie_socks_pass)
    socket.socket = socks.socksocket
    print(socket.socket)

    # PostgreSQL database connection parameters
    db_params = {
        "dbname": "d2r45oj3jf7gs7",
        "user": "ucrol25emqd2ch",
        "password": "p31d791a3fe8bcb5b5102d7b8b43f08ca70ee2cc9d7943c23b4db6b110324346e",
        "host": "ec2-52-2-248-148.compute-1.amazonaws.com",
        "port": 5432,
        "sslcert": "/postgresql.crt",
        "sslkey": "/postgresql.key"
    }

    try:
        # print('conn params 11: ', conn_params)
        # connection = psycopg2.connect(**conn_params)
        # print('conn params: ', conn_params)
        # cursor = connection.cursor()
        # print('proxy type 5')
        # # Example query 
        # query = sql.SQL('SELECT * FROM pgadmin."Prospect" limit 1;')
        # cursor.execute(query)
        # print('proxy type 6')
        # # Fetch results
        # results = cursor.fetchall()
        # print('results:', results)
        # return "private_working"

        # response = requests.get('https://www.google.com')
        # print(response)

        conn = psycopg2.connect(**db_params)
        print("Connected to the database successfully")
        # Perform database operations here

        # Example: Create a cursor and execute a query
        # cursor = conn.cursor()
        # cursor.execute("SELECT 101;")
        # record = cursor.fetchone()
        # print("You are connected to - ", record, "\n")

    except Exception as e:
        print(f"Error: {e}")
        return 'Error'

    # finally:
    #     if connection:
    #         cursor.close()
    #         connection.close()

@app.route('/new')
def newRoute():
    try:
        # Database connection parameters
        db_params = {
            'host': 'ec2-52-2-248-148.compute-1.amazonaws.com',
            'port': 5432,
            'user': 'ucrol25emqd2ch',
            'password': 'p31d791a3fe8bcb5b5102d7b8b43f08ca70ee2cc9d7943c23b4db6b110324346e',
            'database': 'd2r45oj3jf7gs7',
        }

        # Establish a connection to the PostgreSQL database
        connection = psycopg2.connect(**db_params)

        # Create a cursor to execute SQL queries
        cursor = connection.cursor()

        # Example: Execute a simple SQL query
        cursor.execute("SELECT version();")
        version = cursor.fetchone()[0]

        # Close the cursor and connection
        cursor.close()
        connection.close()

        return jsonify({"status": "success", "message": f"Connected to PostgreSQL. Server version: {version}"})

    except psycopg2.Error as e:
        return jsonify({"status": "error", "message": f"Error connecting to the database: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
