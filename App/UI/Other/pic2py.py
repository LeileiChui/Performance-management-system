import base64


def pic2py(picture_names, py_name):
    write_data = []
    for picture_name in picture_names:
        filename = picture_name.replace('.', '_')
        open_pic = open("%s" % picture_name, 'rb')
        b64str = base64.b64encode(open_pic.read())
        open_pic.close()
        write_data.append('%s = "%s"\n' % (filename, b64str.decode()))

    f = open('%s.py' % py_name, 'w+')
    for data in write_data:
        f.write(data)
    f.close()


if __name__ == '__main__':
    pics = ["APP.png",
            "Background.png",
            "Exit.png",
            "Manager.png",
            "NJUPT_Logo.png",
            "Stu.png",
            "Teacher.png",
            "add.png",
            "all.png",
            "class.png",
            "save.png",
            "studen_small.png",
            "teacher_small.png"
            ]
    pic2py(pics, 'memory_pic')
    print("ok")
