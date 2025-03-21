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
To verify if Milvus is running:

```bash
Copy
Edit
docker ps
2️⃣ Install Required Libraries
bash
Copy
Edit
pip install pymilvus pandas numpy
3️⃣ Connect to Milvus
python
Copy
Edit
from pymilvus import connections

connections.connect(alias="default", host="localhost", port="19530")
print("✅ Connected to Milvus!")
pgsql
Copy
Edit

### 🔹 **How This Works?**  
- Any text enclosed within **triple backticks (` ``` `) and a language specifier (`bash`, `python`)** will get a copy button when viewed on GitHub.  
- **No extra plugins or settings needed!** GitHub automatically adds the copy button to **code blocks**.  

Now, when someone views your `README.md` on GitHub, they will see a **copy icon** on the right side of each code block, just like in ChatGPT! 🚀
