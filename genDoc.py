import pdoc

Applications = ['MNIST']
Libs = ['USER', 'TEST', 'DEMO', 'DNN', 'RRAM', 'VECTOR']
Parts = ['BOARD', 'DAC', 'DF', 'EEPROM', 'LED', 'PM', 'TC']
context = pdoc.Context()

def recursive_htmls(mod):
    yield mod.name, mod.html()
    for submod in mod.submodules():
        yield from recursive_htmls(submod)

Applications = [pdoc.Module(lib, context=context) for lib in Applications]
pdoc.link_inheritance(context)
for lib in Applications:
    for lib_name, lib_html in recursive_htmls(lib):
        file = open("docs/Applications/" + lib_name + ".html", "w", encoding="utf-8")
        file.write(lib_html)
        file.close()

Libs = [pdoc.Module(lib, context=context) for lib in Libs]
pdoc.link_inheritance(context)
for lib in Libs:
    for lib_name, lib_html in recursive_htmls(lib):
        file = open("docs/Lib/" + lib_name + ".html", "w", encoding="utf-8")
        file.write(lib_html)
        file.close()

Parts = [pdoc.Module(part, context=context) for part in Parts]
pdoc.link_inheritance(context)
for part in Parts:
    for part_name, part_html in recursive_htmls(part):
        file = open("docs/Board/" + part_name + ".html", "w", encoding="utf-8")
        file.write(part_html)
        file.close()
