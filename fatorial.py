Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:19:30) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def Fatorial(num):
    produto = 1

    while(num > 0):
        produto = produto * num

        num = num - 1

    return produto
