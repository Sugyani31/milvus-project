import time
import numpy as np
from pymilvus import connections, Collection, utility
import pandas as pd

# Connect to Milvus
connections.connect(alias="default", host="localhost", port="19530")

collection_name = "embedding_collection"
collection = Collection(name=collection_name)

# Ensure collection is loaded before searching
collection.load()

# Load embeddings from CSV
df = pd.read_csv("embeddings_data.csv")
embedding_columns = [col for col in df.columns if col != "label"]
embeddings = df[embedding_columns].values.tolist()

# Select first 1000 embeddings for search
num_embeddings_to_test = 1000
batch_size = 100  # Process in batches of 100
nprobe_value = 50  # Adjust to optimize performance

total_time = 0
num_batches = num_embeddings_to_test // batch_size

for i in range(num_batches):
    batch_embeddings = embeddings[i * batch_size: (i + 1) * batch_size]

    # Measure search time for each batch
    start_time = time.time()
    search_result = collection.search(
        data=batch_embeddings,
        anns_field="embedding",
        param={"metric_type": "L2", "params": {"nprobe": nprobe_value}},
        limit=10,  # Get top 10 results per query
        output_fields=["embedding"]
    )
    end_time = time.time()

    batch_time = end_time - start_time
    total_time += batch_time
    print(f"⏱️ Time for batch {i+1}: {batch_time:.6f} seconds")

# Calculate and display average time per batch
average_time = total_time / num_batches
print(f"\n✅ Average time for searching 1000 embeddings in batches of 100: {average_time:.6f} seconds")
