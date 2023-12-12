import collections

text = input()
brackets = '()[]{}'
open, close = brackets[::2], brackets[1::2]
stack = collections.deque()
for c in text:
    if c in open:
        stack.appendleft(open.index(c))
    elif c in close:
        if stack:
            if stack[0] == close.index(c):
                stack.popleft()
            else:
                print('no')
                raise SystemExit
        else:
            print('no')
            raise SystemExit
if len(stack) > 0:
    print('no')
else:
    print('yes')
