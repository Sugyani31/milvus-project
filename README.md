Milvus Experiments


🚀 This repository contains my journey with Milvus, an open-source vector database for similarity search. From setting up Milvus to performing CRUD operations and distance calculations, this repo documents all my work with Milvus from scratch.



## 📖 Overview  

This repository includes:  

✅ Installing & Running Milvus using Docker  

✅ Setting up Milvus and Attu for vector search  

✅ Creating a collection and inserting embeddings  

✅ Performing CRUD operations (Insert, Search, Update, Delete)  

✅ Calculating distances between embeddings (One-to-One and One-to-All)  

✅ Measuring computation time using Milvus and Attu GUI  

✅ Handling large-scale embeddings efficiently  


## 🛠 Installation & Setup  

### 1️⃣ Install Milvus using Docker  
Ensure Docker is installed, then run:  
```bash
 docker pull milvusdb/milvus:latest
docker run -d --name milvus --net host milvusdb/milvus:latest
```
To verify if Milvus is running:
```bash
docker ps
```
### 2️⃣ Install Required Libraries
```bash
pip install pymilvus pandas numpy
```

### 3️⃣ Connect to Milvus
Use the following script to connect to the Milvus server:
```bash
from pymilvus import connections

connections.connect(alias="default", host="localhost", port="19530")
print("✅ Connected to Milvus!")
```

### 📂 Project Structure



milvus-experiments/
│── embeddings_data.csv         # CSV file containing vector embeddings  
│── milvus_setup.py             # Script to initialize Milvus  
│── insert_embeddings.py        # Script to insert embeddings into Milvus  
│── search_embeddings.py        # Query & distance calculation  
│── calculate_distance.py       # Time measurement for searches  
│── README.md                   # Documentation (You are here!)  


### 📊 Milvus Experiments
### 1️⃣ Creating a Collection
```python

from pymilvus import Collection, utility

collection_name = "embedding_collection"
collection = Collection(name=collection_name)

# Check and create index if missing
index_list = utility.list_indexes(collection_name)
if not index_list:
    print("⚠️ No index found. Creating index...")
    index_params = {"metric_type": "L2", "index_type": "IVF_FLAT", "params": {"nlist": 128}}
    collection.create_index(field_name="embedding", index_params=index_params)
    print("✅ Index created successfully.")

collection.load()
```


### 2️⃣ Insert Embeddings from CSV
```python

import pandas as pd

df = pd.read_csv("embeddings_data.csv")
embedding_columns = [col for col in df.columns if col != "label"]
embeddings = df[embedding_columns].values.tolist()
collection.insert(embeddings)
print("✅ Embeddings inserted into Milvus")
```

### 3️⃣ Searching & Distance Calculation
One-to-One Distance Calculation

```python

import time

query_embedding = [embeddings[0]]  # Single embedding

start_time = time.time()
search_result = collection.search(
    data=query_embedding, anns_field="embedding",
    param={"metric_type": "L2", "params": {"nprobe": 10}}, limit=1,
    output_fields=["embedding"]
)
end_time = time.time()

print(f"✅ One-to-One Distance: {search_result[0][0].distance:.6f}")
print(f"⏱️ Time for one-to-one distance: {end_time - start_time:.6f} seconds")
```

### One-to-All Distance Calculation
```python
start_time = time.time()
search_result = collection.search(
    data=query_embedding, anns_field="embedding",
    param={"metric_type": "L2", "params": {"nprobe": 2000}}, limit=2000,
    output_fields=["embedding"]
)
end_time = time.time()
print(f"⏱️ Time for one-to-all distance: {end_time - start_time:.6f} seconds")
```
### Batch Processing for Efficient Distance Calculation

```python

batch_size = 100
total_time = 0

for i in range(0, len(embeddings), batch_size):
    batch = embeddings[i : i + batch_size]
    start_time = time.time()
    search_result = collection.search(
        data=batch, anns_field="embedding",
        param={"metric_type": "L2", "params": {"nprobe": 10}}, limit=10,
        output_fields=["embedding"]
    )
    end_time = time.time()
    total_time += (end_time - start_time)

average_time = total_time / (len(embeddings) / batch_size)
print(f"⏱️ Average search time per batch: {average_time:.6f} seconds")
```



🔥 Key Learnings & Challenges
Milvus Setup & Configuration: Learned how to install and configure Milvus for vector search.

Indexing & Optimization: Explored indexing strategies (IVF_FLAT) and tuning nprobe for better performance.

Batch Processing: Implemented batch-wise embedding search to handle large datasets efficiently.

Handling Errors: Encountered and fixed RESOURCE_EXHAUSTED errors by limiting request sizes.



📌 Next Steps

✅ Optimize indexing techniques (HNSW, IVF_SQ8) for faster searches.

✅ Experiment with different nprobe values and measure accuracy-speed tradeoff.

✅ Perform real-time vector search using Milvus + FastAPI.


🎯 How to Use This Repo?
### 1️⃣ Clone the repository:

```bash
git clone https://github.com/your-username/milvus-experiments.git
cd milvus-experiments
```
### 2️⃣ Install dependencies:

```bash
pip install -r requirements.txt
```

### 3️⃣ Run experiments:

```bash
python3 milvus_setup.py
python3 insert_embeddings.py
python3 search_embeddings.py
```



🤝 Contributing
Feel free to fork this repository and experiment with Milvus! Open an issue if you find any bugs or have suggestions. 🚀


🌟 Acknowledgments
Milvus Documentation
pymilvus GitHub


`
