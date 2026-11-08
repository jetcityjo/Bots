import sys, importlib
sys.path.insert(0, __import__("os").path.dirname(__file__))
import miniapp2
mods = sys.argv[1:] or ["configs_a"]
for m in mods:
    for cfg in importlib.import_module(m).CONFIGS:
        out, probs = miniapp2.build(cfg)
        print(cfg["name"], "OK" if not probs else probs, len(open(out).read()))
