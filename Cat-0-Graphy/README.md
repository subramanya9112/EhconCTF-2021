zip2john password.zip > hash.txt

```
$pkzip2$1*2*2*0*2a*1e*74427fb7*0*42*0*2a*7442*80ca*726d1ea6a78c1035d5b97cb6069f2ca0cf0441f6c5e8260eed80bd93db0641679403dbe00a22a94d1676*$/pkzip2$
```

hashcat -a 0 -m 17210 hash.txt /usr/share/wordlists/rockyou.txt -r ./OneRuleToRuleThemAll.rule --force 

hashcat -a 0 -m 17210 hash.txt /usr/share/wordlists/rockyou.txt -r ./OneRuleToRuleThemAll.rule --force --show

```
EHACON{7h3_5w0rd_0f_d4m0kl35}
```