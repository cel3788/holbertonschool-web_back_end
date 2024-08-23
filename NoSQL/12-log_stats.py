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
    
    # Using aggregation to get counts for all methods in one query
    pipeline = [
        {"$group": {"_id": "$method", "count": {"$sum": 1}}}
    ]
    method_counts = {doc["_id"]: doc["count"] for doc in nginx_collection.aggregate(pipeline)}

    print('Methods:')
    for method in methods:
        count = method_counts.get(method, 0)
        print(f'\tmethod {method}: {count}')

    # Count the number of GET requests to /status
    status_check = nginx_collection.count_documents({"method": "GET", "path": "/status"})
    print(f'{status_check} status check')

if __name__ == "__main__":
    log_stats()
