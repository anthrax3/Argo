import censys
import censys.ipv4
from censys.base import CensysException
import sys,os,re

class censysSearch:
    def censysGath(self):
        path = os.path.abspath(os.path.dirname(sys.argv[0]))
        censys_list = open(path + "/Api/censys_api.txt", "r").read().splitlines()
        if censys_list == []:
            print('no censys api found, please insert a valid one')
            api_censys_uid = input('[****]' + 'type here uid:')
            api_censys_scrt = input('[****]' + 'type here secret:')
            with open(path + "/Api/censys_api.txt", "wb") as api:
                api.write(api_censys_uid + "\n" + api_censys_scrt)
        else:
            uid = censys_list[0]
            secret = censys_list[1]
            try:
                usage = '''+-----------------------------------------------+
|                 Censys search                 |
+-----------------------------------------------+
|                                               |
| (1) Hikvision query       [ App-webs 200 OK ] |
|                                               |
| (2) Rsp device query      [ work in progress] |
|                                               |
| (3) Viola DVR query       [ work in progress] |
|                                               |
| (4) custom query                              |
|                                               |
+-----------------------------------------------+
'''
                print(usage)
                selection = int(input('[-]Choose an option: '))
                if selection == 1:
                    query = 'App-webs 200 OK'
                elif selection == 2:
                    pass
                    #query = 'login.rsp'
                elif selection == 3:
                    pass
                    #query = '/wap.htm'
                elif selection == 4:
                    query = input('[-]Enter your custom query: ')
                for record in censys.ipv4.CensysIPv4(api_id=uid, api_secret=secret).search(query):
                    ip = record['ip']
                    port = record['protocols']
                    port_raw = port[0]
                    port = re.findall(r'\d+', port_raw)
                    with open(path + '/Host/host.txt', "a") as cen:
                        cen.write(ip + ":" + str(port[0]))
                        cen.write("\n")
            except KeyboardInterrupt:
                print("[*]Exiting...")
            except CensysException:
                pass
            except UnboundLocalError:
                print("[No query passed]")