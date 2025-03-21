import time
import pandas as pd
from pymilvus import connections, Collection

# ✅ Connect to Milvus
connections.connect("default", host="localhost", port="19530")

# ✅ Load the Collection
collection = Collection("embedding_collection")
collection.load()  # <-- Add this line to load the collection into memory

# ✅ Load Query Embedding (First Row)
df = pd.read_csv("embeddings_data.csv")
query_embedding = [df.iloc[0, :128].tolist()]

# ✅ Define Search Parameters
search_params = {"metric_type": "L2", "params": {"nprobe": 10}}



# ✅ Measure Time
start_time = time.time()

# ✅ Perform the Search
search_results = collection.search(
    data=query_embedding,
    anns_field="embedding",
    param=search_params,
    limit=5,  # Find top 5 closest vectors
    output_fields=["id"],
)

end_time = time.time()
time_taken = end_time - start_time

# ✅ Print Results
print(f"🔍 Search completed in {time_taken:.6f} seconds")
for hit in search_results[0]:
    print(f"🔹 ID: {hit.id}, Distance: {hit.distance}")
