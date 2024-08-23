#!/usr/bin/env python3
"""Provide statistics about Nginx logs stored in MongoDB."""

from pymongo import MongoClient

def get_log_count(query: dict) -> int:
    """Return the count of logs that match the given query."""
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_logs = client.logs.nginx
    return nginx_logs.count_documents(query)

def print_nginx_logs_stats():
    """Print statistics about the Nginx logs stored in MongoDB."""
    total_logs = get_log_count({})
    print(f"{total_logs} logs")
    
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = get_log_count({'method': method})
        print(f"\tmethod {method}: {count}")
    
    status_check_count = get_log_count({'method': 'GET', 'path': '/status'})
    print(f"{status_check_count} status check")

if __name__ == "__main__":
    print_nginx_logs_stats()
