from WUExport import WebUntisHandler

def main():
    wuh = WebUntisHandler(server='aoide.webuntis.com',
                           username='gloess190117',
                           password='19Gloessl10!2004',
                           school='htbla-weiz',
                           useragent='mgloessl')

    wuh.update_database()
    wuh.print_database()

if __name__ == "__main__":
    main()