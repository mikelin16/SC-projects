"""
File: boggle.py
Name:Mike
----------------------------------------
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'

# Global Variables
dic = {}
# 這個放在global會比較方便，因為很多function都會使用到使用者輸入的字串
current_lst = []
# 開一個list幫忙存去位置點，不能再串字串時，重複串到相同的字
used_position = []
# 開一個數字，紀錄總共找到幾個數字
number = 0


def main():
	"""
	To play a classic game - boggle
	"""
	global current_lst
	read_dictionary()
	for i in range(4):
		rows = input(f"{i + 1} row of letters: ")
		rows = rows.lower().strip()
		if len(rows) != 7:
			print('Illegal input')
			break
		elif (rows[0].isalpha(), rows[2].isalpha(), rows[4].isalpha(), rows[6].isalpha()) \
			and rows[1] == " " and rows[3] == " " and rows[5] == " ":
			current_lst.append([rows[0], rows[2], rows[4], rows[6]])
		else:
			print('Illegal input')
			break
	# current_lst這邊，應該寫成[[a,b,c,d],[a,b,c,d],[a,b,c,d],[a,b,c,d]]會比較好找位置

	# 這邊可以建議你開一個function開始執行boggle
	play_boggle()
	print(f'There are {number} words in total.')


def play_boggle():
	global used_position
	# 先選取第一個字母
	for i in range(4):
		for j in range(4):
			used_position = []
			# 選好字後，先把他串上空字串
			word = ''
			word += current_lst[i][j]
			# 位置要記錄起來
			used_position.append((i, j))
			# 開始recursion
			helper(word, [i, j], [i, j])


def helper(word, old_position, now_position):
	global number, used_position, dic
	old_position = now_position  # 新的位置
	# Base case
	# if has_prefix(word):  # has prefix 如果找不到字，會直接return False，這樣就不會無限迴圈
	if word in dic and len(word) >= 4:
		# # 題目寫說單字長度大於4才要找
		print(f'Found: \"{word}\"')
		# 紀錄總共找到幾個字
		number += 1
		# 找到字後，要把字從字典remove，才不會找到相同的字
		del dic[word]
		# 找到字後，要在呼叫helper，把所有字找完。 ex: room & roomy
		helper(word, old_position, now_position)
	# Not base case
	else:
		for i in range(-1, 2, 1):  # 字串可以串每個位置的+-1
			for j in range(-1, 2, 1):  # 字串可以串每個位置的+-1
				x = i + old_position[0]  # 加上原本位置，確保不會串到空格或其他部分
				y = j + old_position[1]  # 加上原本位置，確保不會串到空格或其他部分
				if 0 <= x < 4 and 0 <= y < 4:
					if (x, y) not in used_position:  # 確認用過的位置不能再用
						used_position.append((x, y))
						# choose
						word += current_lst[x][y]  # 串上新的字母
						now_position = [x, y]  # 存下現在的位置
						# explore
						helper(word, old_position, now_position)  # 往下去找其他字
						# un-chose
						used_position.pop()  # 回到上一層，要把探索過的位置紀錄刪掉，才能串其他字
						word = word[:-1]  # 要把字串刪掉最後一個字


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	with open('dictionary.txt', 'r') as d:
		for line in d:
			line = line.strip()
			dic[line] = 0


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in dic:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
