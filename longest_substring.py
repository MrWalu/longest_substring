# This function returns true if all
# characters in s[i..j] are unique, otherwise returns false
def isUnique(s, i, j):

	visited = [0] * (26)

	for k in range(i, j + 1):
		if (visited[ord(s[k]) - ord('a')] == True):
			return False
			
		visited[ord(s[k]) - ord('a')] = True

	return True

# Returns length of the longest substring
# with unique characters.
def longestUniqueSubstring(s):
	
	n = len(s)
	
	res = 0
	
	for i in range(n):
		for j in range(i, n):
			if (isUnique(s, i, j)):
				res = max(res, j - i + 1)
				
	return res

if __name__ == '__main__':
	
	s = "substring"
	print("The input is ", s)
	
	len = longestUniqueSubstring(s)
	print("The length of the longest non-repeating character substring is ", len)
