text = "X-DSPAM-Confidence:    0.8475"
pos = text.find(':')
# print(pos)
num = text[pos+1:]
# print(num)
value = float(num)
print(value)
