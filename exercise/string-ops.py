# String operations.
st = """There are moments in life when you miss someone so much that
you just want to pick them from your dreams and hug them for real! Dream what
you want to dream;go where you want to go;be what you want to be,because you have
only one life and one chance to do all the things you want to do"""

finding = "want"
idxFirst = st.find(finding)
idxLast = st.rfind(finding)

print(f"'to' 出現 {st.count("to")} 次。")
print(f"'{finding}' 第一次出現在 {idxFirst}，最後一次出現在 {idxLast}。")
print(f"第一次跟最後一次之間的文字：\n{st[idxFirst:idxLast+len(finding)]}")
