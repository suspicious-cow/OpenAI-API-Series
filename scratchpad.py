class PalindromeGenerator:
    def __init__(self, string):
        self.string = string

    def generate_palindrome(self):
        palindrome = self.string + " becomes " + self.string[::-1]
        return palindrome

# Example usage
generator = PalindromeGenerator("oprah")
palindrome = generator.generate_palindrome()
print(palindrome)