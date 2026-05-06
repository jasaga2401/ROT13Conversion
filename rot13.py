
def rot13(message):    
    strOutput = ""
    valid_symbols = "!@#$%^&*()_-+={}[]"

    for element in message:
        
        if (element.islower()):
            
            val = ord(element)
            val += 13            

            if (val > 122):
                val = 96 + (val - 122)
            strOutput += chr(val)

        elif (element.isupper()):
            
            val = ord(element)
            val += 13            

            if (val > 90):
                val = 64 + (val - 90)                

            strOutput += chr(val)

        else:

            strOutput += element

    return strOutput            

# Upper case 65 - 90
# Lower case 97 - 122
message = 'HellZ54'
print(rot13(message))
