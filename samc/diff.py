import difflib

with open("!DOCTYPE50_backup.html", "r", encoding="utf-8") as f1:
    l1 = f1.readlines()
with open("original.html", "r", encoding="utf-8") as f2:
    l2 = f2.readlines()

diff = difflib.unified_diff(l1, l2, fromfile="backup.html", tofile="original.html")
print("".join(diff))
