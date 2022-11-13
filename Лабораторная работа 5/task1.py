from pprint import pprint  # TODO решить с помощью list comprehension и распечатать его

#  keys = ['bin', 'oct', 'hex']
dict_ = [{"bin": bin(i), "oct": oct(i), "hex": hex(i), "dec": i} for i in range(16)]
pprint(dict_)
