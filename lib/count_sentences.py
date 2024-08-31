class MyString:
    def __init__(self, value=""):
        self.value = value  # Use the setter method for initialization

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")
            self._value = ""

    def is_sentence(self):
        """Returns True if the value ends with a period, otherwise False."""
        return self.value.endswith(".")

    def is_question(self):
        """Returns True if the value ends with a question mark, otherwise False."""
        return self.value.endswith("?")

    def is_exclamation(self):
        """Returns True if the value ends with an exclamation mark, otherwise False."""
        return self.value.endswith("!")

    def count_sentences(self):
        """Counts the number of sentences in the value."""
        if not self.value:
            return 0
        
        # Replace punctuation marks with a period for uniformity
        sanitized = self.value.replace("!", ".").replace("?", ".")
        sentences = [s for s in sanitized.split(".") if s.strip()]
        return len(sentences)

# Example usage
string = MyString("This is a string! It has three sentences. Right?")
print(string.is_sentence())     # Output: False
print(string.is_question())     # Output: False
print(string.is_exclamation())  # Output: False
print(string.count_sentences()) # Output: 3
