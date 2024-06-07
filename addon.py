import xbmcplugin
import xbmcgui
import xbmcaddon
import xbmc
import sys

addon_handle = int(sys.argv[1])
xbmcplugin.setContent(addon_handle, 'movies')

addon = xbmcaddon.Addon()
addon_name = addon.getAddonInfo('name')

def listar_canais():
    canais = [
        {"nome": "Canal 1", "url": "http://url-do-canal-1"},
        {"nome": "Canal 2", "url": "http://url-do-canal-2"},
        # Adicione mais canais aqui
    ]

    for canal in canais:
        li = xbmcgui.ListItem(label=canal["nome"])
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=canal["url"], listitem=li, isFolder=False)

    xbmcplugin.endOfDirectory(addon_handle)

if __name__ == '__main__':
    listar_canais()
