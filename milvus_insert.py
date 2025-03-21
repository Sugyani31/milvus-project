import pandas as pd
from pymilvus import connections, Collection

# Connect to Milvus
connections.connect(alias="default", host="localhost", port="19530")

collection_name = "embedding_collection"
collection = Collection(name=collection_name)

# Load data from CSV
df = pd.read_csv("embeddings_data.csv")

# Extract only the first 1000 embeddings (excluding 'label' column)
embedding_columns = [col for col in df.columns if col != "label"]
embeddings = df[embedding_columns].values.tolist()[:1000]  # Select first 1000

# Insert into Milvus
collection.insert([embeddings])

# Flush to save changes
collection.flush()
print(f"✅ Successfully inserted 1000 embeddings into `{collection_name}`!")
print(collection.num_entities)  # Should print at least 1000
