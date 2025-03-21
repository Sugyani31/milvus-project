from pymilvus import connections, Collection

# Connect to Milvus
connections.connect(alias="default", host="localhost", port="19530")

collection_name = "embedding_collection"
collection = Collection(name=collection_name)

# Print collection schema
print("Collection Schema:", collection.schema)
