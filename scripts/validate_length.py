import sys
def validate(text, max_len):
    t_len = len(text)
    m_len = int(max_len)
    if t_len <= m_len: print(f"[PASS] Valid length: {t_len}/{m_len} chars.")
    else: print(f"[FAIL] Too long: {t_len}/{m_len} chars. Must rewrite.")
if __name__ == "__main__":
    if len(sys.argv) > 2: validate(sys.argv[1], sys.argv[2])
