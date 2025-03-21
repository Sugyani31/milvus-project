Milvus Experiments

🚀 This repository contains my journey with Milvus, an open-source vector database for similarity search. From setting up Milvus to performing CRUD operations and distance calculations, this repo documents all my work with Milvus from scratch.



📖 Overview
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
