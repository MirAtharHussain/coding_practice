#1st question:

#keywords: while, if, else, for, continue, const, char,  switch, break, case, int, long, float

#examples input and output:

#input: where    input: for     input: in
#output: No      output: Yes    output: No

#Given keywords, check whether the given input is keyword or not.  if keyword print yes else no


#! usr/bin/python

def check_keyword(keyword_list, param):
	if param in keyword_list:
		print("Yes")
	else:
		print("No")
	
if __name__ =="__main__":
	keyword_lst = ["while", "if", "else", "for", "continue", "const", "char",  "switch", "break", "case", "int", "long", "float"]
	user_input = input("Enter a string")
	check_keyword(keyword_lst, user_input)
	
