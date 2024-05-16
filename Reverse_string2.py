name="Nandhini"    # This line initializes a variable name with the value "Nandhini", 
reverse=''         # This line initializes an empty string reverse, Will store the reversed version of the name string.
i=len(name)-1      # This line initializes a variable i with the length of the name string minus 1. Since indexing in Python starts from 0, len(name) - 1 gives us the index of the last character in the string.
while i>=0:        # This line starts a while loop that continues as long as the value of i is greater than or equal to 0.
    reverse=reverse+name[i] #  Inside the loop, this line appends the character at the index i of the name string to the reverse string. This effectively reverses the characters of the name string.
    i=i-1          # This line decrements the value of i by 1 in each iteration of the loop, moving from the last character of the name string towards the first.
    print(reverse) #  This line prints the current value of the reverse string in each iteration of the loop, effectively showing the reversal process step by step.









    
    
    
    # இந்த வரி "நந்தினி" மதிப்புடன் ஒரு மாறி பெயரை துவக்குகிறது.
    # இந்த வரி ஒரு வெற்று சரத்தைத் தலைகீழாக துவக்குகிறது, பெயர் சரத்தின் தலைகீழ் பதிப்பை சேமிக்கும்.
    # இந்த வரியானது, பெயர் சரத்தின் நீளம் 1 ஐக் கழித்து, ஒரு மாறி ஐ துவக்குகிறது. பைத்தானில் அட்டவணைப்படுத்துதல் 0 இலிருந்து தொடங்குவதால், லென்(பெயர்) - 1 சரத்தின் கடைசி எழுத்தின் குறியீட்டை நமக்கு வழங்குகிறது.
    # i இன் மதிப்பு 0 ஐ விட அதிகமாகவோ அல்லது சமமாகவோ இருக்கும் வரை இந்த வரி ஒரு வேளை வளையத்தைத் தொடங்குகிறது.
    # லூப்பின் உள்ளே, இந்த வரி பெயர் சரத்தின் குறியீட்டு i இல் உள்ள எழுத்தை தலைகீழ் சரத்துடன் இணைக்கிறது. இது பெயர் சரத்தின் எழுத்துக்களை திறம்பட மாற்றுகிறது.
    # இந்த வரியானது லூப்பின் ஒவ்வொரு மறு செய்கையிலும் i இன் மதிப்பை 1 ஆல் குறைக்கிறது, பெயர் சரத்தின் கடைசி எழுத்திலிருந்து முதல் நோக்கி நகரும்.
    # இந்த வரியானது லூப்பின் ஒவ்வொரு மறு செய்கையிலும் தலைகீழ் சரத்தின் தற்போதைய மதிப்பை அச்சிடுகிறது, படிப்படியாக தலைகீழ் செயல்முறையை திறம்பட காட்டுகிறது.