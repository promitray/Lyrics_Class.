import os

path = "/home/ray/python_examples/ML_basics/web_scraping/HTML_scraping/project/"
my_string = []
target = []
direc = ['Britney_Spears', 'MJ', 'Madonna', 'Elvis_Presley', 'Beatles']
#direc = ['Britney_Spears', 'MJ']

for direc in direc:
 for filename in os.listdir(path+direc):
  with open(os.path.join(path+direc, filename), "r") as f:
   string = f.read()
  my_string.append(string)
  if direc == 'Britney_Spears':
   target.append(0)
  if direc == 'MJ':
   target.append(1)
  if direc == 'Madonna':
   target.append(2)
  if direc == 'Elvis_Presley':
   target.append(3)
  if direc == 'Beatles':
   target.append(4)

#print my_string[0]
#print len(target)


from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression

#stop_words = ['a', 'the', 'of', 'and']

cv = CountVectorizer(stop_words = 'english')
vec = cv.fit_transform(my_string)
tf = TfidfTransformer()
vec2 = tf.fit_transform(vec)

print vec2.shape

m = MultinomialNB()
#m = LogisticRegression()

m.fit(vec2, target)
print m.score(vec2, target)


