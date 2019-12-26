# 1~2行是encode()的用法，3-4行是decode()的用法
print('吴枫'.encode('utf-8'))
print('吴枫'.encode('gbk'))
print(b'\xe5\x90\xb4\xe6\x9e\xab'.decode('utf-8'))
print(b'\xe5\x90\xb4\xe6\x9e\xab'.decode('gbk'))
print(b'\xce\xe2\xb7\xe3'.decode('gbk'))
