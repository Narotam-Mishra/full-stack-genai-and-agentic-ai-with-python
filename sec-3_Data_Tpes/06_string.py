
# string in python

chai_type = "Ginger Chai"

customer_name = "Peter"

print(f"Order for {customer_name} : {chai_type} please!")

chai_decription = "Aromatic and Bold"
print(f"first word: {chai_decription[:8]}")
print(f"last word: {chai_decription[12:]}")

# print(f"last word2: {chai_decription[13:]}")
print(f"word reversed: {chai_decription[::-1]}")


label_text = "Chai Spécial"
encoded_label = label_text.encode('utf-8')
print(f"Encoded: {encoded_label}")
print(f"Label text: {label_text}")

decoded_label = encoded_label.decode("utf-8")
print(f"Decoded label: {decoded_label}")