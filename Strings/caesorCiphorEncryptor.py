def caesarCipherEncryptor(string, key):
    # Write your code here.
    alp = {chr(97 + i): i for i in range(26)}
    rev_alp = {v: k for k, v in alp.items()}
    print(alp, rev_alp)
    ans = ""
    for i in string :
        ans = ans + rev_alp[(alp[i]+key)%26]
    return ans
