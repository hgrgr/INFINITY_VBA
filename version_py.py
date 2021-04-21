import json
from oletools.olevba import VBA_Parser, TYPE_OLE, TYPE_OpenXML, TYPE_Word2003_XML, TYPE_MHTML
import argparse
import time

parser = argparse.ArgumentParser("VBA 매크로 PATH")
parser.add_argument('--check_file', required=True, help="악성매크로를 확인할 파일입력")
args = parser.parse_args()
check_file = args.check_file

# check_file = 'clean.docm'
filedata = open(check_file, 'rb').read()
vbaparser = VBA_Parser(check_file, data=filedata)
results = vbaparser.analyze_macros()

if vbaparser.detect_vba_macros():
#     print('Filename    :', filename)
#     print('OLE stream  :', stream_path)
#     print('VBA filename:', vba_filename)

    if not results:
        print("No VBA macros found")
    else:
        with open('blacklist.json', 'r', encoding='utf-8') as j:
                black_list = json.load(j)
                # print(json.dumps(black_list, indent="\t"))

        for(filename, stream_path, vba_filename, vba_code) in vbaparser.extract_macros():
            for key in black_list.keys():
                if key in vba_code.lower():
                    print(black_list[key])
                    print(1111111111111111111111111111111111111111111111111)
                    time.sleep(60)
                    break
else:
    print("No VBA macros found")






# with open('test.json', 'r', encoding='utf-8') as j:
#     black_list = json.load(j)
# # print(json.dumps(black_list, indent="\t"))

# f = open("./olevba_txt/1.txt", 'r', encoding='utf-16 le')

# if "No VBA macros found." not in f:
#     safety = True
#     while safety:
#         line = f.readline()
#         if not line:
#             break
#         for key in black_list.keys():
#             if key in line:
#                 print(black_list[key])
#                 safety = False
#                 break
# f.close()