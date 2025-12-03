import chromadb
from google import genai
from config import GEMINI_API_KEY

# Initialize Gemini embedding client
genai_client = genai.Client(api_key=GEMINI_API_KEY)

# Initialize Chroma
chroma_client = chromadb.Client()

# Create or load the embeddings collection
collection = chroma_client.get_or_create_collection(
    name="embedding_collection"
)

def embed_texts(chunks:list[str]):
    
    ids=[]
    embeddings = []

    for i,chunk in enumerate(chunks):
        ids.append(f"chunk-{i}")

           # Create embeddings via Gemini
        response = genai_client.models.embed_content(
            model="text-embedding-004",
            content=chunk
        )

        embeddings.append(response.embedding)

    collection.add(
        ids=ids,
        embeddings=embeddings,
        documents=chunks)
    
    return {"chunks_added": len(chunks)}


