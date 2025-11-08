import linecache, pathlib, runpy

p = pathlib.Path("t.py")
p.write_text("1 / 0")
try:
    linecache.updatecache(str(p))
    runpy.run_path(str(p))
finally:
    p.unlink()
