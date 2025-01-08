class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()  # Sort the products lexicographically
        res = []  # Result list to store suggestions for each prefix
        
        for i in range(1, len(searchWord) + 1):  # Loop through prefixes of searchWord
            prefix = searchWord[:i]  # Current prefix to match
            char_prefixes = []  # Reset suggestions for this prefix
            
            for prod in products:  # Iterate through sorted products
                if prod.startswith(prefix):  # Check if the product matches the prefix
                    char_prefixes.append(prod)  # Add to suggestions
                if len(char_prefixes) == 3:  # Stop if we already have 3 suggestions
                    break
            
            res.append(char_prefixes)  # Append suggestions for this prefix to the result
        
        return res

# class Solution:
#     def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
#         products.sort()
#         res = []
#         char_prefixes = []
#         for i in range(len(searchWord)):
#             for prod in products:
#                 if prod.startswith(searchWord[i:i+1]) and len(char_prefixes)< 3:
#                     char_prefixes.append(prod)
#             res.append(char_prefixes)
#         return res

        