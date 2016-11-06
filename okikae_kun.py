import sys

argv = sys.argv
temp_body = open(argv[1]).read()
temp_body = temp_body.replace('http://ecx.images-amazon.com/','https://images-fe.ssl-images-amazon.com/')
temp_body = temp_body.replace('http://www.amazon.co.jp/','https://www.amazon.co.jp/')
f = open('output.txt', 'w')
f.write(temp_body)
f.close()
print("finished!")
