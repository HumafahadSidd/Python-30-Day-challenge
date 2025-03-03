"""📢 Day 5 – Daily Python Challenge 🐍
🚀 Challenge:
Aisa Python program likhna hai jo user se ek number lega aur uska sum calculate karega 1 se lekar us number tak. 🔢💡
⿡ sum = n * (n + 1) / 2 ye ek shortcut formula hai jo direct sum de sakta hai. 🔥
⿢ Loop use kar ke bhi solve kar sakte ho (for ya while loop).
⿣ Agar recursion use karna chahtay ho to function ke andar function call karna hoga!
"""



number_user=int(input("Enter the number: "))
sum=number_user*(number_user+1)/2
print(f"The sum of numbers from 1 to {number_user} is: {sum}")


# SECond METHOD:            
# sum=0
# for i in range(1,number_user+1):
#     sum+=i
#  print(f"The sum of numbers from 1 to {number_user} is: {sum}")
 