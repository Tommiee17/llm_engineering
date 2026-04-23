from ingest import fetch_documents, create_chunks, create_embeddings



documents = fetch_documents()
chunks = create_chunks(documents)
create_embeddings(chunks)