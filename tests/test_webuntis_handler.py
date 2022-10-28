import webuntis

try:
    import WUExport
except ImportError as e:
    print('Module import failed %s' % e)

def test_wuhandler_init():
    import WUExport
    assert WUExport.WebUntisHandler
    handler = WUExport.WebUntisHandler(server='aoide.webuntis.com',
                                       username='gloess190117',
                                       password='19Gloessl10!2004',
                                       school='htbla-weiz',
                                       useragent='mgloessl')

def test_wuhandler_classes():
    import WUExport
    assert WUExport.WebUntisHandler
    handler = WUExport.WebUntisHandler(server='aoide.webuntis.com',
                                       username='gloess190117',
                                       password='19Gloessl10!2004',
                                       school='htbla-weiz',
                                       useragent='mgloessl')
    assert handler.classes != None
    assert type(handler.classes) == list
    for lesson in handler.classes:
        