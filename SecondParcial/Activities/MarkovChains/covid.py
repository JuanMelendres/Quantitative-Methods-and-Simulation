import markovify

# Get raw text as string.
with open("text.txt") as f:
    text = f.read()

# Build the model.
text_model = markovify.Text(text)
text_model = text_model.compile()

# Print five randomly-generated sentences
for i in range(6):
    print(text_model.make_sentence())

# Print three randomly-generated sentences of no more than 280 characters
for i in range(3):
    print(text_model.make_short_sentence(280))