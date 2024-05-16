name='Nandhini'
name=name[::-1]   
print(name)

# name=name[::-1]
# The first colon : indicates the beginning of the slicing operation.
# The second colon : indicates the end of the slicing operation.
# The -1 after the second colon specifies the step size of the slicing operation, which indicates that we want to iterate over the string in reverse order.
   # இரண்டாவது பெருங்குடலுக்குப் பின் உள்ள -1 ஸ்லைசிங் செயல்பாட்டின் படி அளவைக் குறிப்பிடுகிறது, இது சரத்தின் மேல் தலைகீழ் வரிசையில் மீண்டும் செய்ய விரும்புகிறோம் என்பதைக் குறிக்கிறது.

# name[::]: This would mean slicing the entire string from the "beginning to the end", without skipping any characters. Essentially, it returns the original string as it is.
   # எந்த எழுத்துகளையும் தவிர்க்காமல், முழு சரத்தையும் "ஆரம்பம் முதல் இறுதி" வரை வெட்டுவதை இது குறிக்கும். அடிப்படையில், அது அசல் சரத்தை அப்படியே திருப்பித் தருகிறது.
# name[::-1]: With the step size as -1, the slicing operation traverses the string in reverse order, starting from the end and moving towards the beginning. This effectively reverses the string.
