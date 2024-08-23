#!/usr/bin/env python3
""" MongoDB Operations with Python using pymongo """
from pymongo import MongoClient

def log_stats():
    """Provides some stats about Nginx logs stored in MongoDB"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    # Get the total number of documents
    n_logs = nginx_collection.count_documents({})
    print(f'{n_logs} logs')

    # Count the number of documents for each HTTP method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print('Methods:')
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f'\tmethod {method}: {count}')

    # Count the number of GET requests to /status
    status_check = nginx_collection.count_documents({"method": "GET", "path": "/status"})
    print(f'{status_check} status check')

if __name__ == "__main__":
    log_stats()
