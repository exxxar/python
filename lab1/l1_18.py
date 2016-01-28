def file2list(text_file):
    try:
        f = open(text_file)
    except IOError:
        print "file %s not exist" %text_file
        return 1

    mas_text = f.readlines()
    f.close()
    return mas_text

if __name__ == "__main__":
    mas_text = file2list("c:\\1\\my_file.txt")
    print mas_