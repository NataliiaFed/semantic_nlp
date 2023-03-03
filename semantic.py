# import the spaCy library
import spacy

# load the English language model
nlp = spacy.load('en_core_web_md')

# use two for loops to undertake a comparison of words
tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
# Cat and monkey seem to be similar because they are both animals;
# Similarly, banana and apple are similar because they are both fruits;
# Interestingly, monkey and banana have a higher similarity than monkey and
# apple. So we can assume that the model already puts together that
# monkeys eat bananas and that is why there is a significant similarity.
# Another interesting fact is that cat does not have any significant similarity
# with any of the fruits although monkey does. So, the model does not
# explicitly seem to recognise transitive relationships in its calculation.

tokens = nlp('cell sell ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
# Despite the fact that words 'cell' and 'sell' are spelled almost the same way and sound the same,
# the model recognizes them as completely different and finds no relationship between them.

tokens = nlp('park parking car forest ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
# 'Park' and 'parking' seem to be similar because of the same base;
# however 'park' is also a city garden which should make it more similar with 'forest'.
# But the similarity with 'forest' is lower, although also quite high.
# Expectedly, 'forest' does not have any significant similarity with 'car',
# and 'car' has similarity with 'parking' and 'park'.


"""Run the example file with the simpler language model ‘en_core_web_sm’
and write a note on what you notice is different from the model
'en_core_web_md'.

Answer: The code in the example file outputs the different extent of similarity when using different models. 
The model ‘en_core_web_sm’ doesn't ship with word vectors and only use context-sensitive tensors, 
and therefore the result of the Doc.similarity method doesn't give useful similarity judgements. """