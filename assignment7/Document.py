class DocumentManager:
    def get_document(self, doc_id):
        return f"Document {doc_id} content here..."

    def search(self, query):
        return f"Searching documents for: {query}"

class DocumentProxy:
    def __init__(self, real_document_manager):
        self.manager = real_document_manager

    def access_document(self, user, doc_id):
        if self.authenticate(user):
            if self.has_permission(user, doc_id):
                self.log_access(user, doc_id)
                return self.manager.get_document(doc_id)
            else:
                return "Access Denied"
        else:
            return "Authentication Failed"

    def authenticate(self, user):
        # Simulate authentication
        return user["authenticated"]

    def has_permission(self, user, doc_id):
        # Simulate permission check
        return user["permission"]

    def log_access(self, user, doc_id):
        print(f"Document {doc_id} accessed by {user['name']}")

    def search_documents(self, query):
        return self.manager.search(query)

# Usage example
real_document_manager = DocumentManager()
document_proxy = DocumentProxy(real_document_manager)

user = {"name": "John Doe", "authenticated": True, "permission": True}
print(document_proxy.access_document(user, 101))
print(document_proxy.search_documents("company report"))
