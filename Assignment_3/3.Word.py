t=input("enter your Paragheraf: ").strip()

c=0 
space=False
for i in t:
  if i==" ":
     if space==False:
       c=c+1
       space=True
  else:
      space=False  


print(f"Word {c+1}")
