class HybridRetriever:
    def retrieve(self, query: str):
        return [{"id": "chunk_1", "score": 0.96, "content": f"Context for {query}"}]
