def calculate(a,operation,b):
  if operation=='+':
    answer=a+b
  elif operation=='-':
    ansawer=a-b
  elif operation=='*':
    answer=a*b
  elif operation=='/' and b==0:
    answer="you can't divide by 0"
  elif operation=="/" and b!=0:
    answer=a/b
  else:
    answer="aise ValueError"
if __name__ == "__main__":
  print(calculate(2,+,3))
  print(calculate(7,-,2))
  print(calculate(2,*,3))
  print(calculate(4,/,1))
  print(calculate(4,/,0))
  print(calculate(2,#,9))
