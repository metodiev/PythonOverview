def test_my_print():
    name_string = "Test My Print and Variables"
    print("Print name_string variable:", name_string)

    print("Test print word length - name_string:", len(name_string))
    print("Test upper case - name_string:", name_string.upper())
    print("Test lower case - name_string:", name_string.lower())
    print("Test title case - name_string:", name_string.title())
    print("Test replace - name_string:", name_string.replace("My", "Your"))

    print("Test replacing whitespaces with underscores:", name_string.replace(" ", "_" ))
    print("Test slicing - first 4 characters:", name_string[0:4])
    print("Test slicing - last 7 characters:", name_string[-7:])

    words = name_string.split()
    joined = "-".join(words)
    print("Test joined", joined)

if __name__ == "__main__":
    test_my_print()