def push(item):
    stack.append(item)

def peek():
    if len(stack) != 0:
        return stack[-1]

def pop():
    if len(stack) != 0:
        item = stack.pop(-1)
        return item

stack = []
push('apple')
push('orange')
push('cherry')
push('pear')
pop()
push('grape')
print(stack)
pop()
print(stack)
