def reverse_sentence(sentence):
    words = sentence.split()  
    reversed_words = words[::-1]  
    reversed_sentence = ' '.join(reversed_words)  
    return reversed_sentence

user_input = input("Enter a sentence: ")
reversed_sentence = reverse_sentence(user_input)
print(reversed_sentence)
