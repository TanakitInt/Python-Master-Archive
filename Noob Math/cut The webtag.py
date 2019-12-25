"""Cut the webtag"""
def main():
    """text"""
    text = str(input())
    webtag_start = "<p>"
    webtag_end = "</p>"
    if text[0:3:] in webtag_start:
        if text[-1:-4:] in webtag_end:
            print("%100s"%text.strip('</p>'))
        else:
            print("%100s"%text.strip('<p>'))
    elif text in webtag_start and text in webtag_end:
        text0 = text.strip('</p>')
        text1 = "%100s"%text0.strip('<p>')
        print(text1)
    else:
        print("%100s"%text)
main()
