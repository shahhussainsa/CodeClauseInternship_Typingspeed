paragraph_dict = {
  "Basic Practice" : "Practice makes typing perfect.",
  "Easy" : "If you`re still not convinced that the English language is full of oddities and conundrums, take a look at these five wacky sentences that are actually grammatically correct.",
	# "Try First" : "Practice makes perfect! Keep typing to improve your skills and speed. You're doing great!",
	"Hard" : "Education is the fundamental process of acquiring knowledge, skills, values, and attitudes. It equips individuals with the tools to navigate the world, fostering personal development and societal progress.",
	
}

def get_paragraph_topic() -> dict:
	'''To get topics name from dictionary'''
	return paragraph_dict.keys()

def get_paragraph_text(para_key) -> str:
	'''To get topic\'s text from dictionary key'''
	return paragraph_dict.get(para_key)