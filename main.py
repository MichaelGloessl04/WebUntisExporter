from WUExport import WebUntisHandler
import toolbox

def main():
    wuh = WebUntisHandler(server='aoide.webuntis.com',
                           username='gloess190117',
                           password='19Gloessl10!2004',
                           school='htbla-weiz')

    wuh.login()

    print(toolbox.json_to_dict("C://Code\WebUntisExporter//toolbox//teacher_id_name.json"))

    wuh.logout()

if __name__ == "__main__":
    main()