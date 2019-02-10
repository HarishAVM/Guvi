h = input()
print( ''.join([ h[a:a+2][::-1] for a in range(0, len(h), 2) ]))
