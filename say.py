import re

dc = {"can","do","have","was","would"}

speech = "I Do as programmer"

def speech_correction(words, speech):
	# Your code here
	words_r = dict({})

	for word in words:
		word = word.lower()
		if word == "can":
			words_r["can"] = "can't"
			words_r["can't"] = "can"
			continue

		words_r[word] = word + "n't"
		words_r[word + "n't"] = word

		words_r[word + "'ve"] = word + "n've"
		words_r[word + "n've"] = word + "'ve"

	def replace_word(match):
		word_to_check = match.group(0)

		if word_to_check.lower() in words_r:
			new_word = words_r[word_to_check.lower()]

			if word_to_check.isupper():
				return new_word.upper()

			elif word_to_check[0].isupper() and not word_to_check.isupper():
				return new_word.capitalize()

			else:
				return new_word

		return word_to_check

	return re.sub(r"[a-zA-Z']+", replace_word, speech)


print(speech_correction(dc, speech))