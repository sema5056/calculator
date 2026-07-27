def calculate(a,operation,b):
  if operation=='+':
    answer=a+b
    return answer
  elif operation=='-':
    ansawer=a-b
    return answer
  elif operation=='*':
    answer=a*b
    return answer
  elif operation=='/' and b==0:
    answer="you can't divide by 0"
    return answer
  elif operation=="/" and b!=0:
    answer=a/b
    return answer
  else:
    raise ValueError("Unknown operation")"
if __name__ == "__main__":
  print(calculate(2,+,3))
  print(calculate(7,-,2))
  print(calculate(2,*,3))
  print(calculate(4,/,1))
  print(calculate(4,/,0))
  print(calculate(2,#,9))
