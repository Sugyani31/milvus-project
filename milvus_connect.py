from pymilvus import connections

# Connect to Milvus
connections.connect("default", host="localhost", port="19530")

# Verify the connection
print("✅ Successfully connected to Milvus!")
