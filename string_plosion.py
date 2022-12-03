def string_splosion(str):
    if len(str) >= 0:
        for i in range(0, len(str)):
            for j in range(0, i+1):
                print(str[j], end="")


string_splosion('Code')
# string_splosion('abc')
# string_splosion('ab')
