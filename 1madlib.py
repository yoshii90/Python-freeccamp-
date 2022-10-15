# # string concatenation ( how to put strings together )
# # suppose we want to create a string that says " subscribe to ______"
# youtuber = "Name" # some string varibale


 # a few ways to do this

# print("subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")

adj1 = input("Adjective: ")
adj2 = input("Adjective: ")
verb1 = input("Verb: ")
fp =input("Famous person: ")

madlib = f"Computer science is so {adj1}! It makes me so excited all the time because \
I love to {adj2}! Stay hydrated and {verb1}! It makes me feel like {fp}!"

print(madlib)
