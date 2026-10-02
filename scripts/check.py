#!/usr/bin/env python3
"""校验 Shadowrocket_fish.conf：规则/策略组引用、本仓库 .list 文件是否存在。"""
import os, re, sys

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
s = open(os.path.join(root, "Shadowrocket_fish.conf"), encoding="utf-8").read()
sec, cur = {}, None
for l in s.split("\n"):
    m = re.match(r"^\[(.+)\]$", l)
    if m:
        cur = m.group(1); sec[cur] = []; continue
    if cur and l.strip() and not l.startswith("#"):
        sec[cur].append(l)

groups = {l.split(" = ", 1)[0] for l in sec["Proxy Group"]}
builtin = {"PROXY", "DIRECT", "REJECT"}
errors = []
for l in sec["Proxy Group"]:
    name, val = l.split(" = ", 1)
    for p in val.split(",")[1:]:
        if p.startswith("policy-regex-filter="):
            break
        if p.startswith("policy-select-name="):
            p = p.split("=", 1)[1]
        if p not in groups | builtin:
            errors.append(f"策略组 {name} 引用了不存在的 {p}")
for l in sec["Rule"]:
    p = l.split(",")
    if p[0] == "FINAL":
        pol = p[1]
    else:
        pol = p[-1] if p[-1] != "no-resolve" else p[-2]
    if pol not in groups | builtin:
        errors.append(f"规则指向不存在的策略: {l[:80]}")
    m = re.search(r"fishingfish/AI-Works/refs/heads/main/(\S+?\.list)", l)
    if m and not os.path.exists(os.path.join(root, m.group(1))):
        errors.append(f"缺少文件: {m.group(1)}")
if "<<<<<<<" in s or ">>>>>>>" in s:
    errors.append("配置里还有冲突标记")
print("\n".join(errors) if errors else "OK: 无引用错误")
sys.exit(1 if errors else 0)
