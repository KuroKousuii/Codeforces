s = input()
st = set()
for i in s:
    st.add(i)
print("CHAT WITH HER!" if len(st) % 2 == 0 else "IGNORE HIM!")