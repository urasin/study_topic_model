# https://qiita.com/shuntaroy/items/b0e557be3406a9b09ade
def ngram(words, n):
  return [tuple(words[i:i + n]) for i in range(len(words) - n + 1)]
  

# print(ngram("this is a pen", 1)[0][1])
print(len(tuple([1])))

# ngram コーパス参考
# https://www.slideshare.net/moaikids/ngram-4770283
