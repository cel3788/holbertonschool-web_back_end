from pymongo import MongoClient

def log_stats():
    # Connect to the MongoDB server
    client = MongoClient('localhost', 27017)
    
    # Access the logs database and the nginx collection
    db = client.logs
    collection = db.nginx
    
    # Get the total number of documents
    total_logs = collection.count_documents({})
    
    # Count the number of documents for each HTTP method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {}
    for method in methods:
        method_counts[method] = collection.count_documents({"method": method})
    
    # Count the number of documents with method=GET and path=/status
    status_check_count = collection.count_documents({"method": "GET", "path": "/status"})
    
    # Print the results
    print(f"{total_logs} logs")
    print("Methods:")
    for method in methods:
        print(f"\tmethod {method}: {method_counts[method]}")
    print(f"{status_check_count} status check")

if __name__ == "__main__":
    log_stats()
