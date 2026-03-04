
daily_visitors = [1_250, 980, 1_430, 2_100, 1_890, 760, 430,
                  1_320, 1_050, 1_780, 2_250, 1_970, 810, 510]
total=0
average=0
highest=0
max=daily_visitors[0]
min=daily_visitors[0]

for n in daily_visitors:
  total=total+n
  average=total//len(daily_visitors)
  if n>1_500:
    highest=highest+1
  if n>max:
    max=n
  if n<min:
    min=n

print("Total numbers of visitors:",total)
print("Average daily visitors:",average)
print("Number of days > 1500:",highest)
print("Highest single day visitors:",max)
print("Lowest single day visitors:",min)