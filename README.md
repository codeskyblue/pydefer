## pydefer

en: golang defer implements in python.

zh: golang��defer��python�е�ʵ��

## ʹ�þ���

    @pydefer.wrapper
    def hi(name = 'mei zi'):
        pydefer.defer(printf, 'what is your tel number, %s', name)
        print 'hi', name

    hi()

    # output order
    # hi mei zi
    # what is your tel number, meizi
