from pymilvus import connections, Collection, CollectionSchema, FieldSchema, DataType

# Connect to Milvus
connections.connect(alias="default", host="localhost", port="19530")

# Define collection name
collection_name = "embedding_collection"

# Define schema (Updated for 2048-dimensional embeddings)
id_field = FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True)
embedding_field = FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=2048)  # Changed dim to 2048

schema = CollectionSchema(fields=[id_field, embedding_field], description="Embedding collection")

# Create the collection
collection = Collection(name=collection_name, schema=schema)

# Create an index before loading
index_params = {"index_type": "IVF_FLAT", "metric_type": "L2", "params": {"nlist": 1024}}
collection.create_index(field_name="embedding", index_params=index_params)

# Load collection into memory
collection.load()

print(f"Collection '{collection_name}' has been created with 2048-dimensional embeddings.")
