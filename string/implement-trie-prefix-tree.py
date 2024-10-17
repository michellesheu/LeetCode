class TrieNode:
    def __init__(self):
        self.links = [None] * 26
        self.is_end = False
    
    def contains_key(self, ch: str) -> bool:
        return self.links[ord(ch) - ord('a')] is not None

    def get(self, ch: str) -> 'TrieNode':
        return self.links[ord(ch) - ord('a')]
    
    def put(self, ch: str, node: 'TrieNode') -> None:
        self.links[ord(ch) - ord('a')] = node

    def set_end(self) -> None:
        self.is_end = True

    def get_end(self) -> bool:  # Changed method name to avoid conflict
        return self.is_end

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if not node.contains_key(ch):
                node.put(ch, TrieNode())
            node = node.get(ch)
        node.set_end()
        
    def search_prefix(self, word: str) -> TrieNode:
        node = self.root
        for ch in word:
            if node.contains_key(ch):
                node = node.get(ch)
            else:
                return None
        return node
        
    def search(self, word: str) -> bool:
        node = self.search_prefix(word)
        return node is not None and node.get_end()  # Updated to use new method name

    def startsWith(self, prefix: str) -> bool:
        node = self.search_prefix(prefix)  # Removed underscore
        return node is not None