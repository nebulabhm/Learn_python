args = ['gcc', 'hello.c', 'world.c']
# args = ['clean']
# args = ['gcc']

match args:
    # 濡傛灉浠呭嚭鐜癵cc锛屾姤閿�:
    case ['gcc']:
        print('gcc: missing source file(s).')
    # 鍑虹幇gcc锛屼笖鑷冲皯鎸囧畾浜嗕竴涓枃浠�:
    case ['gcc', file1, *files]:
        print('gcc compile: ' + file1 + ', ' + ', '.join(files))
    # 浠呭嚭鐜癱lean:
    case ['clean']:
        print('clean')
    case _:
        print('invalid command.')