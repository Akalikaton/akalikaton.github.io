# 20230311
    P: 0310中，txt转html可行，但0304无法增加html css样式
    猜测0304行数少，codecs.open后并未及时关闭，导致后面写入css无法读取
    解决，使用with codecs.open，自带关闭